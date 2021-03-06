from blogconfig import logo, website_domain, blog_location

def generate_opengraph_meta(title, url):
    return f'''
<!-- OpenGraph Meta Tags -->
<meta property="og:title" content="{title} | ThatOneLukas's Blog!">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{logo}">
<meta property="og:image:secure_url" content="{logo}" />
<meta property="og:image:type" content="image/png" />
<meta property="og:image:width" content="400" />
<meta property="og:image:height" content="400" />
<meta property="og:image:alt" content="ThatOneLukas's Logo" />
<meta property="og:site_name" content="ThatOneLukas's Website!">
<meta property="og:description" content="Homemade programmer">
    '''.strip()

def generate_html_meta(url, author, tags):
    return f'''
<!-- HTML Meta Tags -->
<meta name="description" content="Homemade programmer">
<meta name="keywords" content="{', '.join(tags)}"/>
<meta name="copyright" content="ThatOneLukas">
<meta name="author" content="{author}">
<meta name="designer" content="ThatOneLukas">
<meta name="owner" content="ThatOneLukas">
<meta name="url" content="{url}">
<meta name="identifier-URL" content="{url}">
    '''.strip()

def generate_twitter_meta(title, url):
    return f'''
<!-- Twitter Meta Tags -->
<meta name="twitter:card" content="summary_large_image">
<meta property="twitter:domain" content="{website_domain}">
<meta property="twitter:url" content="{url}">
<meta name="twitter:title" content="{title} | ThatOneLukas's Blog!">
<meta name="twitter:description" content="Homemade programmer">
<meta name="twitter:image" content="{logo}">
    '''.strip()

def generate_head_html(title, stylesheets):
    stylesheets_html = '\n'.join(map(lambda x: '<link rel="stylesheet" href="/static/' + x + '" />', stylesheets))
    return f'''
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} | ThatOneLukas's Blog!</title>

<!-- Apple Meta Tags -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta content="yes" name="apple-touch-fullscreen" />
<meta name="apple-mobile-web-app-status-bar-style" content="black">

<link rel="stylesheet" href="/static/styles.css" />
{stylesheets_html}
    '''.strip()

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

def generate_html(head, content):
    return f'''
<!DOCTYPE html>
<!-- index.html -->
<html lang="en">
    <head>
        {head}
    </head>
    <body>
        <header class="header">
            <div class="innerHeader container">
                <h1><a href="/" class="lukas-header">Lukas's Website!</a></h1>
                <a href="/blog">Blogs</a>
            </div>
        </header>
        <main class="main content" style="padding-top: 7rem; padding-bottom: 7rem;">
            {content}
        </main>
        <footer id="footer">
            <div class="container">
                <h2>(c) Copyright ThatOneLukas 2021</h2>
            </div>
        </footer>
    </body>
</html>
    '''.strip()