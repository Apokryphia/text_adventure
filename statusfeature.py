from flask import Flask, render_template, request, redirect, url_for


def statusbar():
    values = {
        "current_health": 100,
        "current_money": 50
    }
    return values

