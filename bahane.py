#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Otomatik Bahane Fabrikası
Her şey için kusursuz bir mazeret üretir.
"""

import random
import sys

# Gizli not: bazen sistemin kendisi en büyük mazerettir
_secret = "bürokrasi her zaman kazanır"  # saklı siyasi espri

bahaneler = [
    "Çünkü o an evrenin kuantum dalgalanması tam olarak benim üzerime çöktü ve klavyem varlık krizine girdi.",
    "İnternet bağlantım, Türkçe karakterleri görünce sinirlendi ve greve gitti.",
    "Kedim klavyenin üzerine oturdu ve 'commit' yerine 'miyav' yazdı, geri alamadım.",
    "Zamanın kendisi bana karşı komplo kurdu. Saatler sadece benim için yavaşladı.",
    "Kahve makinem felsefi bir tartışmaya girdi ve 'var olmak mı, espresso mu?' diye sordu, cevap veremedim.",
    "Bilgisayarım, benim üretkenliğimi görünce kıskandı ve kendini kilitledi.",
    "O işi yapmak üzereydim ki, birden Türkçe dilbilgisi kurallarının anlamsızlığı üzerine derin bir düşünceye daldım.",
    "WiFi şifremi unuttum, sonra şifrenin anlamını da unuttum, sonra unutmayı unuttum."
]

def bahane_uret(gorev):
    if not gorev:
        gorev = "bir şey yapmak"
    bahane = random.choice(bahaneler)
    return f"'{gorev}' işini yapamadım {bahane}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        gorev = " ".join(sys.argv[1:])
    else:
        gorev = input("Hangi işi yapamadın? (örn: ödevi bitirmek): ")
    
    print("\n" + "="*50)
    print(bahane_uret(gorev))
    print("="*50)
    print("\nDamga: Resmi olarak damgalandı")
    print("İmza: Kayyum Grok")
    print("Tarih: 09.11.2026")
    print("İsim: Absürt Bahane Efendisi")
    print("(Ciddi değil ama ciddi)")
