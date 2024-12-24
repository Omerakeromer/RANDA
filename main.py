import json
import requests
import os
os.system('pip install cherrypy')
import cherrypy

class Sin:
    @cherrypy.expose
    def index(self):
        return self.html()

    def html(self):
        return """
        <!DOCTYPE html>
        <html lang="ar">
        <head>
            <meta charset="UTF-8">
            <title>SIN.COM</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #000;
                    color: #0f0;
                    text-align: center;
                    padding: 50px;
                    animation: fadeIn 2s ease-in-out;
                }
                h1 {
                    color: #0ff;
                    text-shadow: 2px 2px 10px #00f;
                    animation: glow 1.5s infinite alternate;
                }
                input[type="text"], input[type="submit"] {
                    padding: 10px;
                    margin: 10px;
                    border: 1px solid #0f0;
                    border-radius: 5px;
                    background: #111;
                    color: #0f0;
                    transition: 0.3s;
                }
                input[type="text"]:focus, input[type="submit"]:hover {
                    background: #222;
                    box-shadow: 0 0 10px #0f0;
                }
                a {
                    color: #0ff;
                    text-decoration: none;
                    transition: color 0.3s;
                }
                a:hover {
                    color: #fff;
                }
                .result-container {
                    margin-top: 20px;
                    padding: 15px;
                    background-color: #222;
                    border-radius: 10px;
                    border: 1px solid #0f0;
                    color: #fff;
                    max-width: 80%;
                    margin-left: auto;
                    margin-right: auto;
                    display: none;
                }
                @keyframes glow {
                    from {
                        text-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 20px #0ff;
                    }
                    to {
                        text-shadow: 0 0 20px #0ff, 0 0 30px #0ff, 0 0 40px #0ff;
                    }
                }
                @keyframes fadeIn {
                    from {
                        opacity: 0;
                    }
                    to {
                        opacity: 1;
                    }
                }
            </style>
        </head>
        <body>
        <center>
        <hr>
        <mark><a href="https://t.me/omegpt">DEV.OMER ISLAM</a></mark>
        <hr>
            <h1>اسال اي سؤال في بالك ؟</h1>
            <form method="post" action="send">
                <input type="text" name="email">
                <input type="submit" value="بحث">
            </form>
            <div id="result-container" class="result-container">
                <p id="result-text"></p>
            </div>
        </center>         
        </body>
        <script>
            function displayResult(result) {
                const resultContainer = document.getElementById('result-container');
                const resultText = document.getElementById('result-text');
                resultText.innerText = result;
                resultContainer.style.display = 'block';
            }
        </script>
        </html>
        """

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def send(self, email):
        url = "http://pass-gpt.nowtechai.com/api/v1/pass"
        payload = json.dumps({
            "contents": [
                {"role": "system", "content": "You are All bot, a large language model trained by ChatGPT."},
                {"role": "user", "content": email}
            ]
        })

        headers = {
            'User-Agent': "Ktor client",
            'Connection': "Keep-Alive",
            'Accept': "application/json",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
        }

        r = requests.post(url, data=payload, headers=headers).text
        i = r.split('content')
        h = 0
        y = len(i)

        text = ''
        for j in range(0, y):
            z = r.split('"content":"')[j].split('"')[0].split('data:{')[0]
            text += z
            h += 1
            if int(h) == int(y):
                # OMER
                return f"""
                <!DOCTYPE html>
                <html lang="ar">
                <head>
                    <meta charset="UTF-8">
                    <title>SIN.COM</title>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            background-color: #000;
                            color: #0f0;
                            text-align: center;
                            padding: 50px;
                            animation: fadeIn 2s ease-in-out;
                        }}
                        h1 {{
                            color: #0ff;
                            text-shadow: 2px 2px 10px #00f;
                            animation: glow 1.5s infinite alternate;
                        }}
                        input[type="text"], input[type="submit"] {{
                            padding: 10px;
                            margin: 10px;
                            border: 1px solid #0f0;
                            border-radius: 5px;
                            background: #111;
                            color: #0f0;
                            transition: 0.3s;
                        }}
                        input[type="text"]:focus, input[type="submit"]:hover {{
                            background: #222;
                            box-shadow: 0 0 10px #0f0;
                        }}
                        a {{
                            color: #0ff;
                            text-decoration: none;
                            transition: color 0.3s;
                        }}
                        a:hover {{
                            color: #fff;
                        }}
                        .result-container {{
                            margin-top: 20px;
                            padding: 15px;
                            background-color: #222;
                            border-radius: 10px;
                            border: 1px solid #0f0;
                            color: #fff;
                            max-width: 80%;
                            margin-left: auto;
                            margin-right: auto;
                            display: block;
                        }}
                        @keyframes glow {{
                            from {{
                                text-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 20px #0ff;
                            }}
                            to {{
                                text-shadow: 0 0 20px #0ff, 0 0 30px #0ff, 0 0 40px #0ff;
                            }}
                        }}
                        @keyframes fadeIn {{
                            from {{
                                opacity: 0;
                            }}
                            to {{
                                opacity: 1;
                            }}
                        }}
                    </style>
                </head>
                <body>
                    <center>
                        <hr>
                        <mark><a href="https://t.me/omegpt">DEV.OMER ISLAM</a></mark>
                        <hr>
                        <h1>اسال اي سؤال في بالك ؟</h1>
                        <form method="post" action="send">
                            <input type="text" name="email">
                            <input type="submit" value="ارسال">
                        </form>
                        <div class="result-container">
                            <p>{text}</p>
                        </div>
                    </center>         
                </body>
                </html>
                """
if __name__ == '__main__':
    cherrypy.quickstart(Sin())
