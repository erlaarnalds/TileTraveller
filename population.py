folk_nu=307357870

#set gildi sem segir hve margar sek eru i einu ari
ar_sek=365*24*60*60
ar_sek_float=float(ar_sek)

#utreikningar a gefnum gildum
faeding=ar_sek_float/7
daudi=ar_sek_float/13
innflytjandi=ar_sek_float/35

#faum input fra notenda um hve morg ar skulu liða, breytum þvi svo i float
# (f reikninga) og int (fyrir print)
ar_str=input('Years: ')
ar_float=float(ar_str)
ar_int=int(ar_str)

if ar_float<0:
    print('Invalid input!')
else:
    folksfjoldi=folk_nu+ar_float*(faeding-daudi+innflytjandi)
    folksfjoldi_int=int(folksfjoldi)
    print('New population after', ar_int, 'years is', folksfjoldi_int)


