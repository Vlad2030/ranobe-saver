import asyncio
import aiohttp
import os
import re
from zipfile import ZipFile

async def ftch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def dl_archive():
    def zipiter(arr):
        i = 1
        amax = len(arr)
        
        if amax == 0:
            return
        elif amax == 1:
            yield [None, arr[0], None]
            return
        
        yield [None, arr[0], arr[1]]
        
        while i <= amax - 2:
            yield [arr[i - 1], arr[i], arr[i + 1]]
            i += 1
        
        yield [arr[i - 1], arr[i], None]
    
    def html_template(title, head, body, ch_p, ch_c, ch_n, ch_all):
        return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <style>
        body {{
            font-weight: 100;
            font-family: -webkit-pictograph;
            font-size: 18px;
            line-height: 1;
            text-align: center;
            word-break: break-word;
            margin: 0 auto;
            padding: 25px 5vw;
            background-color: #434751;
            color: #dbdbdb;
            min-height: calc(100vh - 50px);
        }}

        * {{
            tab-size: 4 !important;
            scrollbar-width: thin; /* Firefox scrollbar 8px */
        }}
        /* Chrome scrollbar */
        *::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
            background-color: transparent;
        }}
        *::-webkit-scrollbar-thumb {{
            background-color: #8888;
        }}
        *::-webkit-scrollbar:hover {{
            background-color: #8883;
        }}

        div {{
            line-height: 1.4;
            font-weight: 700;
            font-size: 24px;
        }}
        div ~ div:last-of-type {{
            margin-bottom: 40px;
        }}

        p {{
            margin-bottom: 12px;
            text-align: left;
        }}

        a {{
            display: block;
            user-select: none;
            color: inherit;
            text-decoration: none;
            border-radius: 10px;
        }}
        a.prev, a.next {{
            position: fixed;
            bottom: 5px;
            width: 4vw;
            height: 30vh;
            font-size: 2vw;
            line-height: 30vh;
            border: 1px solid #dbdbdb;
            z-index: 5;
        }}
        a.prev {{
            left: 5px;
        }}
        a.next {{
            right: 5px;
        }}
        a:hover {{
            background-color: #dbdbdb30;
        }}

        nav {{
            position: fixed;
            right: 0;
            /* top: 0; */
            bottom: 0;
            max-width: 520px;
            display: grid;
            padding: 10px 14px;
            gap: 2px;
            align-content: start;
            background-color: hsla(223, 9.5%, 22%, 0);
            text-align: left;
            font-weight: 500;
            font-size: 16px;
            max-height: 40px;
            overflow: hidden;
            z-index: 3;
            transition: .3s ease;
        }}
        nav::before {{
            content: "Оглавление";
            display: block;
            font-size: 20px;
            padding: 15px 15px 20px 15px;
            cursor: pointer;
        }}
        nav:focus-within {{
            max-height: calc(100vh - 20px);
            overflow: auto;
            background-color: hsla(223, 9.5%, 22%, 1);
            z-index: 6;
        }}
        nav > a {{
            padding: 10px 14px;
        }}
        nav > a:hover, nav > a.current {{
            background-color: hsla(223, 9.5%, 13%, 0.3);
        }}
    </style>
</head>
<body>
{head}
{body}
<script>
    const chapters = {ch_all},
          current = {ch_c},
          nav = document.createElement("nav"),
          a_p = document.createElement("a"),
          a_n = document.createElement("a");

    a_p.href = `v${ch_p['chapter_volume']}_${str(ch_p['chapter_number']).zfill(3)}.html`;
    a_n.href = `v${ch_n['chapter_volume']}_${str(ch_n['chapter_number']).zfill(3)}.html`;

    a_p.classList.add("prev");
    a_n.classList.add("next");

    a_p.innerText = "←";
    a_n.innerText = "→";

    if ({ch_p}) document.body.appendChild(a_p);
    if ({ch_n}) document.body.appendChild(a_n);

    for (let ch of chapters) {{
        const cd = document.createElement("a");
        cd.innerText = `Том ${ch['chapter_volume']} Глава ${ch['chapter_number']} - ${ch['chapter_name']}`;
        cd.href = `v${ch['chapter_volume']}_${str(ch['chapter_number']).zfill(3)}.html`;

        if (ch['chapter_id'] === current['chapter_id']) cd.classList.add("current");

        nav.appendChild(cd);
    }}

    nav.setAttribute("tabindex", "0");

    document.body.appendChild(nav);
</script>
</body>
</html>'''

    chapters_url = "https://ranobelib.me" + window.location.pathname
    async with aiohttp.ClientSession() as session:
        chapters = await ftch(session, chapters_url)
        chapters_list = re.search(r"window\.__DATA__\s*=\s*({.*});", chapters).group(1)
        chapters_list = json.loads(chapters_list)["props"]["initialState"]["chapters"]["list"]
        chapters_list.reverse()
        last_chapter = chapters_list[-1]

        with ZipFile("archive.zip", "w") as zip:
            for p, c, n in zipiter(chapters_list):
                print(f"DL volume {c['chapter_volume']} chapter {c['chapter_number']} of volume {last_chapter['chapter_volume']} chapter {last_chapter['chapter_number']}")

                url = f"https://ranobelib.me{window.location.pathname}/v{c['chapter_volume']}/c{c['chapter_number']}"
                response = await ftch(session, url)
                soup = BeautifulSoup(response, "html.parser")
                dom_head = soup.find("a", class_="reader-header-action")
                dom_txt = soup.find(class_="reader-container")

                zip.writestr(
                    f"chapters_html/v{c['chapter_volume']}_{str(c['chapter_number']).zfill(3)}.html",
                    html_template(f"{dom_head.find(class_='reader-header-action__text')!.text} - Том {c['chapter_volume']} Глава {c['chapter_number']}", dom_head.text.strip(), dom_txt.text, p, c, n, chapters_list)
                )

                zip.writestr(
                    f"chapters_txt/v{c['chapter_volume']}_{str(c['chapter_number']).zfill(3)}.txt",
                    f"{dom_head.text.strip()}\n\n{''.join([c.text + '\n' for c in dom_txt.children])}"
                )

async def main():
    await dl_archive()

asyncio.run(main())