# █ █ ▒ ░

import time, os

class colour:
    Green = "\u001b[32m"
    Yellow = "\u001b[33m"
    Blue = "\u001b[34m"
    Magenta = "\u001b[35m"
    White = "\u001b[37m"
    Red = "\u001b[31m"

W = f"{colour.White}█{colour.Red}" # white
G = f"{colour.White}▒{colour.Red}" # grey

f1 = f"""{colour.Red}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{G}▒░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}▒░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░"""

f2 = f"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{W}▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{G}▒░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}▒░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░"""

f3 = f"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▒░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▒▒▒▒{W}{W}{G}{W}{W}{W}▒░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{W}▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{G}▒░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}▒░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░"""

f4 = f"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░▒█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░▒█▒░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░▒█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░▒█▒░░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░▒░░▒░░░░▒{W}{G}{W}{W}{W}▒░░░░▒░▒█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▒█▒▒{W}{W}{G}{W}{W}{W}▒░▒█▒░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░▒▒▒▒▒▒█▒{W}{G}{W}{W}{W}▒▒█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{W}█▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{G}▒░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}▒░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░"""

f5 = f"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░▒█▒░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▒░░░░░░░░░░░░░
░▒█▒░░░░░░░░░▒▒▒▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░▒▒▒▒▒▒▒{W}{W}{G}{W}{W}{W}▒▒▒▒░░░░░░░░░░░▒░░░░▒█▒░░░░░░░░░░░░░░░░░░░░░░░
░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{W}▒▒▒█▒░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░
▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{G}▒░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}▒░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░"""

f6 = f"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▒▒▒▒▒{W}{G}{W}{W}{W}▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{W}▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▒░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░▒█▒░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{G}▒░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}▒░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░"""

f7 = f"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{G}▒░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}▒░░░░░░░░░░▒░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░▒█▒"""

f8 = f"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{W}▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{G}▒░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}▒░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░"""

f9 = f"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{G}▒░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}▒░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░"""

f10 = f"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{G}▒░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}▒░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░"""

f11 = f"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{G}▒░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}▒░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░"""

f12 = f"""░░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{G}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{G}▒░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}░{W}{W}{W}{W}{W}▒░░░░░░░░░░░░
{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒░░░▒{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}{W}▒▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒{W}{W}{W}{W}{W}▒▒▒▒▒░░░░░░░░"""

frames = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.01)