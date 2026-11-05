from pathlib import Path

base = Path(__file__).resolve().parent
html_path = base / 'myapp' / 'templates' / 'index.html'
text = html_path.read_text(encoding='utf-8')

if '{% load static %}' not in text:
    text = text.replace('<!DOCTYPE html>', '{% load static %}\n<!DOCTYPE html>', 1)

replacements = {
    'css/bootstrap.min.css': "{% static 'css/bootstrap.min.css' %}",
    'css/aos.css': "{% static 'css/aos.css' %}",
    'css/swiper-bundle.min.css': "{% static 'css/swiper-bundle.min.css' %}",
    'css/all.min.css': "{% static 'css/all.min.css' %}",
    'css/magnific-popup.css': "{% static 'css/magnific-popup.css' %}",
    'css/style.css': "{% static 'css/style.css' %}",
    'js/jquery-3.7.1.min.js': "{% static 'js/jquery-3.7.1.min.js' %}",
    'js/bootstrap.bundle.min.js': "{% static 'js/bootstrap.bundle.min.js' %}",
    'js/aos.js': "{% static 'js/aos.js' %}",
    'js/swiper-bundle.min.js': "{% static 'js/swiper-bundle.min.js' %}",
    'js/jquery.magnific-popup.min.js': "{% static 'js/jquery.magnific-popup.min.js' %}",
    'js/main.js': "{% static 'js/main.js' %}",
    'img/banner-img.jpg': "{% static 'images/banner-img.jpg' %}",
    'img/menu/1.jpg': "{% static 'images/menu/1.jpg' %}",
    'img/menu/2.jpg': "{% static 'images/menu/2.jpg' %}",
    'img/menu/3.jpg': "{% static 'images/menu/3.jpg' %}",
    'img/menu/4.jpg': "{% static 'images/menu/4.jpg' %}",
    'img/menu/5.jpg': "{% static 'images/menu/5.jpg' %}",
    'img/menu/6.jpg': "{% static 'images/menu/6.jpg' %}",
    'img/category/1.jpg': "{% static 'images/category/1.jpg' %}",
    'img/category/2.jpg': "{% static 'images/category/2.jpg' %}",
    'img/category/3.jpg': "{% static 'images/category/3.jpg' %}",
    'img/category/4.jpg': "{% static 'images/category/4.jpg' %}",
    'img/category/5.jpg': "{% static 'images/category/5.jpg' %}",
    'img/category/6.jpg': "{% static 'images/category/6.jpg' %}",
    'img/about1.jpg': "{% static 'images/about1.jpg' %}",
    'img/about2.jpg': "{% static 'images/about2.jpg' %}",
    'img/off-img.jpg': "{% static 'images/off-img.jpg' %}",
    'img/portfolio/work1.jpg': "{% static 'images/portfolio/work1.jpg' %}",
    'img/portfolio/work2.jpg': "{% static 'images/portfolio/work2.jpg' %}",
    'img/portfolio/work3.jpg': "{% static 'images/portfolio/work3.jpg' %}",
    'img/portfolio/work4.jpg': "{% static 'images/portfolio/work4.jpg' %}",
    'img/portfolio/work5.jpg': "{% static 'images/portfolio/work5.jpg' %}",
    'img/chefs/1.jpg': "{% static 'images/chefs/1.jpg' %}",
    'img/chefs/2.jpg': "{% static 'images/chefs/2.jpg' %}",
    'img/chefs/3.jpg': "{% static 'images/chefs/3.jpg' %}",
    'img/chefs/4.jpg': "{% static 'images/chefs/4.jpg' %}",
    'img/testimonial/1.jpg': "{% static 'images/testimonial/1.jpg' %}",
    'img/testimonial/2.jpg': "{% static 'images/testimonial/2.jpg' %}",
    'img/testimonial/3.jpg': "{% static 'images/testimonial/3.jpg' %}",
    'img/testimonial/4.jpg': "{% static 'images/testimonial/4.jpg' %}",
    'img/blog/1.jpg': "{% static 'images/blog/1.jpg' %}",
    'img/blog/2.jpg': "{% static 'images/blog/2.jpg' %}",
    'img/blog/3.jpg': "{% static 'images/blog/3.jpg' %}",
}

for old, new in replacements.items():
    text = text.replace(old, new)

html_path.write_text(text, encoding='utf-8')
print('Template static paths updated')
