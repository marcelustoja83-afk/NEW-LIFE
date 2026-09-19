from flask import Flask, render_template_string

app = Flask(__name__)

# ============================================================
# USTAWIENIA PRODUKTU
# ============================================================

PRODUCT_NAME = "NEW LIFE"
PRODUCT_PRICE = "19,99 zł"

PRODUCT_DESCRIPTION = (
    "7-dniowy e-book o budowaniu odwagi, pewności siebie "
    "i robieniu małych kroków w stronę zmian."
)

AUTHOR = "Marcel Chrzanowski i Marcel Okoń"

PAYHIP_URL = "https://payhip.com/NEWLIFEMCMO"


# ============================================================
# GŁÓWNY SZABLON
# ============================================================

PAGE = """
<!DOCTYPE html>
<html lang="pl">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<meta name="description"
content="NEW LIFE — Zbuduj odwagę. Przestań się ukrywać. Zacznij żyć.">

<title>{{ title }} | NEW LIFE</title>

<style>

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;

    background:
        radial-gradient(
            circle at 50% -10%,
            #292929 0%,
            #0d0d0d 35%,
            #050505 70%
        );

    color: white;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    min-height: 100vh;
}

a {
    color: inherit;
    text-decoration: none;
}

.navbar {
    position: sticky;
    top: 0;
    z-index: 1000;

    background:
        rgba(5,5,5,0.90);

    backdrop-filter:
        blur(18px);

    border-bottom:
        1px solid #252525;
}

.navbar-inner {
    max-width: 1150px;
    margin: auto;
    padding: 18px 25px;

    display: flex;
    align-items: center;
    justify-content: space-between;
}

.logo {
    font-size: 20px;
    font-weight: bold;
    letter-spacing: 6px;
}

.nav-links {
    display: flex;
    gap: 25px;
}

.nav-links a {
    color: #999;
    font-size: 14px;
}

.nav-links a:hover {
    color: white;
}

.button {
    display: inline-flex;

    align-items: center;
    justify-content: center;

    padding: 16px 28px;

    border-radius: 9px;
    border: none;

    font-weight: bold;

    cursor: pointer;

    transition:
        transform 0.2s,
        background 0.2s;
}

.button-main {
    background: white;
    color: black;
}

.button-main:hover {
    background: #dddddd;
    transform: translateY(-3px);
}

.button-dark {
    background: #161616;
    border: 1px solid #444;
    color: white;
}

.button-dark:hover {
    background: #222;
}

.hero {
    max-width: 1150px;

    min-height: 90vh;

    margin: auto;

    padding: 90px 25px;

    display: grid;

    grid-template-columns:
        1.1fr 0.9fr;

    gap: 70px;

    align-items: center;
}

.small-label {
    color: #777;

    font-size: 12px;

    letter-spacing: 5px;

    margin-bottom: 25px;
}

.hero h1 {
    margin: 0;

    font-size:
        clamp(65px, 11vw, 145px);

    line-height: 0.85;

    letter-spacing: 8px;
}

.hero h2 {
    font-size:
        clamp(24px, 4vw, 42px);

    line-height: 1.2;

    margin:
        35px 0 25px;
}

.hero-description {
    color: #999;

    font-size: 18px;

    line-height: 1.8;

    max-width: 650px;
}

.hero-buttons {
    display: flex;

    gap: 15px;

    flex-wrap: wrap;

    margin-top: 35px;
}

.book-cover {
    min-height: 560px;

    padding: 45px;

    border:
        1px solid #383838;

    border-radius: 20px;

    display: flex;

    flex-direction: column;

    justify-content: space-between;

    background:
        radial-gradient(
            circle at 80% 10%,
            #444,
            transparent 35%
        ),

        linear-gradient(
            145deg,
            #242424,
            #080808
        );

    box-shadow:
        0 40px 100px
        rgba(0,0,0,0.55);
}

.cover-top {
    color: #888;
    letter-spacing: 4px;
    font-size: 12px;
}

.cover-title {
    font-size: 68px;

    font-weight: bold;

    letter-spacing: 7px;

    line-height: 0.9;
}

.cover-subtitle {
    color: #aaa;

    font-size: 17px;

    line-height: 1.7;
}

.cover-author {
    color: #777;

    font-size: 12px;

    letter-spacing: 2px;
}

.section {
    max-width: 1050px;

    margin: auto;

    padding: 110px 25px;
}

.section-header {
    text-align: center;

    margin-bottom: 60px;
}

.section-header h2 {
    margin: 0 0 20px;

    font-size:
        clamp(35px, 6vw, 65px);
}

.section-header p {
    max-width: 700px;

    margin: auto;

    color: #888;

    line-height: 1.8;

    font-size: 18px;
}

.cards {
    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 20px;
}

.card {
    padding: 32px;

    border:
        1px solid #292929;

    border-radius: 16px;

    background:
        rgba(255,255,255,0.025);

    transition: 0.25s;
}

.card:hover {
    transform:
        translateY(-5px);

    border-color:
        #444;

    background:
        rgba(255,255,255,0.05);
}

.card-number {
    color: #666;

    font-size: 13px;

    letter-spacing: 3px;

    margin-bottom: 25px;
}

.card h3 {
    margin: 0 0 15px;

    font-size: 23px;
}

.card p {
    color: #888;

    line-height: 1.7;

    margin: 0;
}

.days {
    display: grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap: 15px;
}

.day {
    padding: 28px;

    border:
        1px solid #292929;

    border-radius: 14px;

    background:
        #0b0b0b;

    transition: 0.2s;
}

.day:hover {
    border-color:
        #444;

    transform:
        translateY(-3px);
}

.day-number {
    color: #666;

    font-size: 12px;

    letter-spacing: 4px;

    margin-bottom: 13px;
}

.day h3 {
    margin:
        0 0 10px;

    font-size: 20px;
}

.day p {
    color: #777;

    margin: 0;

    line-height: 1.6;
}

.info-grid {
    display: grid;

    grid-template-columns:
        1fr 1fr;

    gap: 20px;
}

.info-box {
    padding: 35px;

    border:
        1px solid #292929;

    border-radius: 16px;

    background:
        #0b0b0b;
}

.info-box h3 {
    margin-top: 0;

    font-size: 25px;
}

.info-box p {
    color: #888;

    line-height: 1.8;
}

.buy-section {
    padding:
        120px 25px;

    text-align: center;
}

.buy-box {
    max-width: 600px;

    margin: auto;

    padding:
        60px 35px;

    border:
        1px solid #3a3a3a;

    border-radius: 22px;

    background:
        radial-gradient(
            circle at top,
            #292929,
            #0a0a0a 65%
        );

    box-shadow:
        0 30px 80px
        rgba(0,0,0,0.45);
}

.buy-box h2 {
    font-size: 45px;

    margin:
        10px 0 20px;
}

.price {
    font-size: 75px;

    font-weight: bold;

    margin:
        20px 0;
}

.buy-description {
    color: #888;

    line-height: 1.7;

    margin-bottom: 30px;
}

.buy-note {
    color: #555;

    font-size: 12px;

    margin-top: 20px;
}

.faq {
    max-width: 800px;

    margin: auto;
}

.faq-item {
    padding:
        27px 0;

    border-bottom:
        1px solid #292929;
}

.faq-item h3 {
    margin:
        0 0 12px;

    font-size: 19px;
}

.faq-item p {
    color: #888;

    line-height: 1.7;

    margin: 0;
}

.footer {
    border-top:
        1px solid #222;

    text-align: center;

    padding:
        65px 20px;

    color: #555;
}

.footer strong {
    color: #aaa;

    letter-spacing: 5px;
}

.footer p {
    margin:
        13px 0;
}

@media(max-width: 800px) {

    .hero {
        grid-template-columns: 1fr;

        padding-top: 70px;
    }

    .cards {
        grid-template-columns: 1fr;
    }

    .days {
        grid-template-columns: 1fr;
    }

    .info-grid {
        grid-template-columns: 1fr;
    }

    .nav-links {
        display: none;
    }

    .book-cover {
        min-height: 470px;
    }

    .cover-title {
        font-size: 52px;
    }

    .price {
        font-size: 55px;
    }

}

</style>

</head>

<body>

<nav class="navbar">

<div class="navbar-inner">

<a href="/" class="logo">
NEW LIFE
</a>

<div class="nav-links">

<a href="#o-ebooku">
O E-BOOKU
</a>

<a href="#dni">
7 DNI
</a>

<a href="#faq">
FAQ
</a>

<a href="#kup">
KUP
</a>

</div>

</div>

</nav>

{{ content|safe }}

<footer class="footer">

<strong>
NEW LIFE
</strong>

<p>
Zbuduj odwagę. Przestań się ukrywać. Zacznij żyć.
</p>

<p>
Stworzone przez Marcel Chrzanowski i Marcel Okoń.
</p>

</footer>

</body>

</html>
"""


# ============================================================
# STRONA GŁÓWNA
# ============================================================

@app.route("/")
def home():

    content = f"""

<section class="hero">

<div>

<div class="small-label">
E-BOOK • 7 DNI
</div>

<h1>
NEW<br>
LIFE
</h1>

<h2>
Zbuduj odwagę.<br>
Przestań się ukrywać.<br>
Zacznij żyć.
</h2>

<p class="hero-description">

NEW LIFE to 7-dniowy e-book stworzony dla osób,
które chcą zatrzymać się na chwilę, spojrzeć
na swoją codzienność z innej perspektywy
i zacząć robić małe kroki w stronę zmian.

</p>

<div class="hero-buttons">

<a href="#kup"
class="button button-main">

KUP E-BOOK

</a>

<a href="#o-ebooku"
class="button button-dark">

DOWIEDZ SIĘ WIĘCEJ

</a>

</div>

</div>


<div class="book-cover">

<div class="cover-top">
E-BOOK • 7 DNI
</div>

<div class="cover-title">
NEW<br>
LIFE
</div>

<div class="cover-subtitle">

Zbuduj odwagę.<br>
Przestań się ukrywać.<br>
Zacznij żyć.

</div>

<div class="cover-author">

{AUTHOR.upper()}

</div>

</div>

</section>


<section class="section"
id="o-ebooku">

<div class="section-header">

<div class="small-label">
O E-BOOKU
</div>

<h2>
Zacznij od jednego kroku.
</h2>

<p>

Nie musisz zmieniać całego życia w jeden dzień.
NEW LIFE skupia się na małych decyzjach,
działaniu i budowaniu własnej drogi.

</p>

</div>

<div class="cards">

<div class="card">

<div class="card-number">
01
</div>

<h3>
7 dni
</h3>

<p>

Siedem rozdziałów prowadzących
przez kolejne tematy związane
z odwagą, działaniem i rozwojem.

</p>

</div>


<div class="card">

<div class="card-number">
02
</div>

<h3>
Praktyczne zadania
</h3>

<p>

Każdy dzień zawiera zadanie,
które możesz wykonać we własnym
tempie i dopasować do swojego życia.

</p>

</div>


<div class="card">

<div class="card-number">
03
</div>

<h3>
Nowa perspektywa
</h3>

<p>

Zatrzymaj się, zastanów nad swoją
codziennością i zacznij świadomie
podejmować kolejne decyzje.

</p>

</div>

</div>

</section>


<section class="section"
id="dni">

<div class="section-header">

<div class="small-label">
ZAWARTOŚĆ
</div>

<h2>
7 dni. 7 kroków.
</h2>

<p>

Każdy dzień skupia się na innym
elemencie drogi.

</p>

</div>

<div class="days">

<div class="day">
<div class="day-number">DZIEŃ 01</div>
<h3>Podejmij decyzję</h3>
<p>Ten moment, kiedy masz już dość.</p>
</div>

<div class="day">
<div class="day-number">DZIEŃ 02</div>
<h3>Wyjdź poza swoje cztery ściany</h3>
<p>Wyjdź z miejsca, w którym się ukrywasz.</p>
</div>

<div class="day">
<div class="day-number">DZIEŃ 03</div>
<h3>Przestań żyć pod spojrzeniem innych</h3>
<p>Nie musisz cały czas przejmować się opinią innych.</p>
</div>

<div class="day">
<div class="day-number">DZIEŃ 04</div>
<h3>Zrób coś, czego wcześniej się bałeś</h3>
<p>Odwaga zaczyna się od działania.</p>
</div>

<div class="day">
<div class="day-number">DZIEŃ 05</div>
<h3>Zacznij budować pewność siebie</h3>
<p>Pewność siebie buduje się krok po kroku.</p>
</div>

<div class="day">
<div class="day-number">DZIEŃ 06</div>
<h3>Naucz się działać mimo gorszych dni</h3>
<p>Nie każdy dzień musi być idealny.</p>
</div>

<div class="day">
<div class="day-number">DZIEŃ 07</div>
<h3>Twoje nowe życie zaczyna się teraz</h3>
<p>To dopiero początek.</p>
</div>

<div class="day">
<div class="day-number">KONIEC</div>
<h3>Nie wracaj do życia, które Cię ograniczało</h3>
<p>Zakończenie całej drogi.</p>
</div>

</div>

</section>


<section class="section">

<div class="section-header">

<div class="small-label">
DLA CIEBIE
</div>

<h2>
Małe kroki. Własne tempo.
</h2>

<p>

Nie musisz robić wszystkiego naraz.
Najważniejsze jest rozpoczęcie.

</p>

</div>

<div class="info-grid">

<div class="info-box">

<h3>
Jeżeli chcesz coś zmienić
</h3>

<p>

Jeżeli masz wrażenie, że utknąłeś
w rutynie albo chcesz spróbować
czegoś nowego, NEW LIFE może być
punktem wyjścia do refleksji
i działania.

</p>

</div>

<div class="info-box">

<h3>
Jeżeli chcesz zacząć działać
</h3>

<p>

Nie chodzi o perfekcję.
Chodzi o małe, realistyczne kroki,
które możesz wykonywać we własnym
tempie.

</p>

</div>

</div>

</section>


<section class="buy-section"
id="kup">

<div class="buy-box">

<div class="small-label">
NEW LIFE • E-BOOK
</div>

<h2>
Twój pierwszy krok
</h2>

<div class="price">
{PRODUCT_PRICE}
</div>

<p class="buy-description">

{PRODUCT_DESCRIPTION}

</p>

<a href="{PAYHIP_URL}"
class="button button-main">

KUP E-BOOK

</a>

<div class="buy-note">

Produkt cyfrowy • PDF • Płatność przez Payhip

</div>

</div>

</section>


<section class="section"
id="faq">

<div class="section-header">

<div class="small-label">
FAQ
</div>

<h2>
Najczęstsze pytania
</h2>

</div>

<div class="faq">

<div class="faq-item">

<h3>
Czym jest NEW LIFE?
</h3>

<p>

To cyfrowy e-book podzielony
na siedem dni. Każdy dzień
zawiera tekst oraz praktyczne
zadanie.

</p>

</div>


<div class="faq-item">

<h3>
Czy e-book jest papierowy?
</h3>

<p>

Nie. NEW LIFE jest produktem
cyfrowym.

</p>

</div>


<div class="faq-item">

<h3>
Ile jest rozdziałów?
</h3>

<p>

E-book składa się z siedmiu dni
oraz zakończenia.

</p>

</div>


<div class="faq-item">

<h3>
W jakim formacie będzie e-book?
</h3>

<p>

NEW LIFE jest dostępny jako
plik PDF.

</p>

</div>


<div class="faq-item">

<h3>
Jak wygląda zakup?
</h3>

<p>

Po kliknięciu przycisku KUP E-BOOK
przechodzisz do strony Payhip,
gdzie możesz dokonać zakupu.
Po udanej płatności Payhip obsługuje
dostarczenie produktu cyfrowego.

</p>

</div>

</div>

</section>


<section class="section"
style="text-align:center;">

<div class="small-label">
NEW LIFE
</div>

<h2 style="
font-size:clamp(45px,7vw,80px);
margin:0 0 25px;
">

Zacznij od siebie.

</h2>

<p style="
color:#888;
font-size:18px;
line-height:1.8;
max-width:650px;
margin:auto;
">

Zbuduj odwagę.
Przestań się ukrywać.
Zacznij żyć.

</p>

<div style="
margin-top:35px;
">

<a href="{PAYHIP_URL}"
class="button button-main">

KUP E-BOOK

</a>

</div>

</section>

"""

    return render_template_string(
        PAGE,
        title="E-book",
        content=content
    )


# ============================================================
# URUCHOMIENIE
# ============================================================

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5001
    )
