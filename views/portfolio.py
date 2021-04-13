from flask import Flask, render_template, url_for, flash, redirect, request, Blueprint

portfolio = Blueprint('portfolio', __name__)


@portfolio.route('/')
def main():
    return render_template('main.html')


@portfolio.route('/about')
def about():
    return render_template('about.html')


@portfolio.route('/skills')
def skills():
    return render_template('skills.html')


@portfolio.route('/experience')
def experience():
    return render_template('experience.html')


@portfolio.route('/contact')
def contact():
    return render_template('contact.html')
