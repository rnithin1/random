def make_name():
  from random import randint
  nomen = ['preet', 'meet', 'jodh', 'windar', 'jeet', 'deep', 'noor', 'bir',
        'mohan']
  praenomen = ['raman', 'aman', 'kamal', 'jas', 'simran', 'gur', 'har', 'man', 'bal',
        'nav', 'sukh', 'kul', 'prabh', 'gagan', 'mohan']
  cognomen = ['kaur', 'singh']
  caesar = ['bhai', 'gyani', 'sardar', 'sardarji', 'jarnail']
  tribus = ['ahluwalia', 'bhullar', 'bhindranwale', 'saini', 'khatri', 'aurora',
        'kamboj', 'ramdasia', 'chuhra', 'labana', 'kumhar', 'jatt', 'bhat',
        'bahadur', 'kahluria']
  title = ""
  caste = ""
  first = praenomen[randint(0,len(praenomen) - 1)]
  second = nomen[randint(0, len(nomen) - 1)]
  name = cognomen[randint(0,len(cognomen) - 1)]
  if randint(0, 3) == 2:
    caste = tribus[randint(0,len(tribus) - 1)] + " "
  if randint(0, 2) == 2:
    title = caesar[randint(0,len(caesar) - 1)] + " "
  if first == second:
    first = praenomen[randint(0, len(praenomen) - 1)]
  naam = title + first + second + " " + name + " " + caste
  return naam.title().strip()

make_name()
