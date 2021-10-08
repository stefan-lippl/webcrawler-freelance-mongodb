# TODO's

1. Freelancermap unter dem Punkt Firma:

   Problem:
   Zum einen wird ein a-tag in einem span verwendet, zum anderen wird der Text - also der Name der Firma -
   direkt in den span geschrieben.

   Lösung:
   Eine Kontrollstruktur einbauen die überprüft ob ein a tag in dem span verfügbar ist oder nicht. Wenn nein
   soll der Text direkt aus dem span extrahiert werden. Wenn ja soll der Firmenname aus dem a-tag genommen
   werden.

   Ansatz:
   company = response.xpath(...)
   try:
   if company == None:
   company = response.xpath(new_xpath_with_a_tag)
   if company == None:
   company = 'None'
   except:
   company = 'None'
