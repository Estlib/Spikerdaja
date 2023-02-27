from pyflowchart import Flowchart
with open('moving_dot_3.17.py') as f:
    code = f.read()
fc = Flowchart.from_code(code)
print(fc.flowchart())
fail = open("flowchart.txt","w") # Loome uue faili
# Kirjutame rea faili ja lisame reavahetuse (\n)
fail.write(fc.flowchart())
fail.close() # Sulgeme faili