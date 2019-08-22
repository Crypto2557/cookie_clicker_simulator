"""Registers the different competitions"""
from cookie_clicker.competitions.impl import ProfitCompetition
from cookie_clicker.competitions.impl import RevenueCompetition
from cookie_clicker.competitions.impl import CPSCompetition
from cookie_clicker.competitions.impl import TimeToRevenueCompetition
from cookie_clicker.competitions.mathematician import Mathematician

ProfitCompetition()
RevenueCompetition()
CPSCompetition()
TimeToRevenueCompetition()

Mathematician()
