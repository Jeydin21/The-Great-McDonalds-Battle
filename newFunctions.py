import time
import os
from misc import *

def attack():
  attackStatement = ""
  damageStatement = ""

  karenHealth = int(read("enemyhp"))
  chance = random.randrange(11)
  attack = random.randint(10, 20)

  if chance >= 0 and chance <= 1:
    attackStatement += choosestatement("enemydodge")
    damageStatement += "You did not deal any damage to Karen."

  elif chance >= 2 and chance <= 8:
    attackStatement += choosestatement("youattack")
    damageStatement += "You dealt " + str(attack) + " damage to Karen!"
    newHealth = karenHealth - attack
    write("enemyhp", newHealth)

  else:
    attackStatement += choosestatement("youcrit")
    damageStatement += "You dealt " + str(attack * 2) + " damage to Karen (" + str(attack) + " x 2)!"
    newHealth = karenHealth - (attack * 2)
    write("enemyhp", newHealth)

  attackData = {
    "attackStatement": attackStatement,
    "damageStatement": damageStatement,
    "karenHealth": int(read("enemyhp")),
    "yourHealth": int(read("yourhealth"))
  }

  return attackData


def enemyStrike():
  attackedStatement = ""
  damagedStatement = ""

  yourHealth = int(read("yourhealth"))
  chance = random.randrange(11)
  attack = random.randint(10, 20)

  if chance >= 0 and chance <= 1:
    attackedStatement += choosestatement("youdodge")
    damagedStatement += "Karen did not deal any damage to you."

  elif chance >= 2 and chance <= 8:
    attackedStatement += choosestatement("enemyattack")
    damagedStatement += "You took " + str(attack) + " damage!"
    newHealth = yourHealth - attack
    write("yourhealth", newHealth)

  else:
    attackedStatement += choosestatement("enemycrit")
    damagedStatement += "She dealt " + str(attack * 2) + " damage to you (" + str(attack) + " x 2)!"
    newHealth = yourHealth - (attack * 2)
    write("yourhealth", newHealth)

  enemyStrikeData = {
    "attackedStatement": attackedStatement,
    "damagedStatement": damagedStatement,
    "karenHealth": int(read("enemyhp")),
    "yourHealth": int(read("yourhealth"))
  }

  return enemyStrikeData


def endGame():
  write("yourhealth", 100)
  write("enemyhp", 100)


def chooseSurrender():
  chance = random.randrange(101)

  if chance >= 50:
    return "success"
  
  elif chance <= 49:
    return "fail"


def getHealth():
  yourHealth = read("yourhealth")
  karenHealth = read("enemyhp")
  healthData = {"yourHealth": yourHealth, "karenHealth": karenHealth}
  
  return healthData
