from flask import Flask, render_template, url_for, flash, redirect, request, Blueprint

portfolio = Blueprint('portfolio', __name__)


@portfolio.route('/')
def base():
    palette = ['#01aff3', '#6bf700', '#eff109', '#f64e0c', '#cb268b']
    return render_template('base.html', colors=palette)
