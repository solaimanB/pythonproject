prijs_totaal = 12
aantal = 3
prijs_per_product = prijs_totaal / 3
btw_precentage = prijs_per_product / 100 * 21
prijs_per_product_zonder_btw = prijs_per_product - btw_precentage
prijs_totaal_zonderbtw = 3 * prijs_per_product_zonder_btw
prijs_totaal2 = "prijs intotaal: "
aantal2 = "aantal: "
prijs_per_product2 = "prijs per product:"
btw_precentage2 = "btw precentage: "
prijs_per_product_zonder_btw2 = 'Prijs per product zonder btw: '
prijs_totaal_zonderbtw2 = "prijs totaal zonder btw: "
print(prijs_totaal2,prijs_totaal)
print(aantal2,aantal)
print(prijs_per_product2,prijs_per_product)
print(btw_precentage2,btw_precentage)
print(prijs_per_product_zonder_btw2,prijs_per_product_zonder_btw)
print(prijs_totaal_zonderbtw2,prijs_totaal_zonderbtw)
