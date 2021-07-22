from head_gen import generate_head_html


# Private functions

def generate_html_raw(head, content):
    return f'''
<!DOCTYPE html>
<!-- index.html -->
<html lang="en">
    <head>
        {head}
    </head>
    <body>
        <div id="content">
            <section class="top-section">
                <header id="header">
                    <a href="/"><h1>Lukas's Blog</h1></a>
                    <nav id="nav">
                        <a href="/">Home</a>
                        <a href="/about">About</a>
                        <a href="/blog">Articles</a>
                    </nav>
                </header>
                <main id="main">
                    {content}
                </main>
            </section>
            <footer id="footer">
                <div class="footer-left">Copyright © 2021 ThatOneLukas</div>
                <div class="footer-right"><a href="/">Home</a></div>
            </footer>
        </div>
    </body>
</html>
    '''.strip()

# Public functions


def twitter_logo(color):
    return f'''
<svg version="1.1" height="25px" viewBox="0 0 231.104 231.104">
    <g><path style="fill: {color};" d="M4.453,173.33c9.763-1.192,19.663,0.092,29.426-1.512c4.904-0.779,9.396-2.429,13.842-4.171
    c-11-7.058-20.901-15.125-30.113-24.796c-3.3-3.438-0.917-9.213,3.896-9.35c3.942,0.183,7.792-0.137,11.55-0.917
    c-9.58-12.146-17.005-25.209-22.78-39.876c-1.558-3.942,3.025-7.929,6.738-6.738c2.154,0.871,4.354,1.467,6.6,1.925
    c-6.829-16.409-8.25-32.955-4.446-51.106c0.871-4.171,6.371-5.179,9.167-2.429c21.909,21.541,49.593,31.9,79.202,36.85
    c-2.613-20.259,11.78-41.801,30.663-48.86c15.676-5.821,36.714-1.833,47.256,11.367c7.059-4.446,16.821-5.913,24.659-7.288
    c4.125-0.688,8.113,3.346,5.684,7.425c-2.842,4.767-5.546,9.854-8.525,14.713c6.05-1.788,12.284-2.888,18.517-3.667
    c4.492-0.596,7.196,6.325,3.759,9.075c-7.288,5.821-14.53,12.467-22.276,17.784c-0.229,51.472-15.263,94.649-61.235,123.937
    c-38.319,24.477-109.546,20.352-142.867-12.97H3.124c-1.467-0.367-2.246-1.467-2.521-2.658c-1.283-1.925-0.367-4.308,1.329-5.225
    C2.574,174.063,3.399,173.467,4.453,173.33z"/></g>
</svg>
    '''.strip()


def generate_html(title, stylesheets, url, author, tags, content, description):
    return generate_html_raw(generate_head_html(title, stylesheets, url, author, tags, description), content)
