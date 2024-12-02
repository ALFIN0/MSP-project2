# Výstup na základě výsledků získaných z kódu

1) **Odhady parametrů Weibullova rozdělení:**
   - **Shape (MLE)**: 6.17
   - **Scale (MLE)**: 7.43

   To znamená, že parametry Weibullova rozdělení pro dobu zaměstnání v oboru byly odhadnuty takto:
   - Tvar (shape) = 6.17, což naznačuje, že doba zaměstnání v oboru má pravděpodobnostní rozdělení s vysokým "sklonem" směrem k nižším hodnotám. Vysoký tvar znamená, že většina absolventů zůstává v oboru po relativně krátkou dobu.
   - Měřítko (scale) = 7.43 let, což představuje průměrnou délku doby, po kterou absolventi zůstávají v oboru.

2) **Test hypotézy:**
   - **Test poměru věrohodnosti** (Likelihood ratio test) ukázal **statistiku 619.08** a **p-hodnotu 0.0**. To znamená, že nulová hypotéza (že data následují exponenciální rozdělení, tedy tvar = 1) je vyvržena s velmi vysokou statistickou významností. Na základě těchto výsledků je jasné, že exponenciální rozdělení není vhodný model pro tato data, protože Weibullovo rozdělení lépe popisuje chování doby zaměstnání.

3) **Bodové odhady:**
   - **Průměrná doba zaměstnání v oboru** (mean) je odhadnuta na **8.63 let**. To znamená, že průměrná doba, po kterou absolventi VUT zůstávají v oboru, je přibližně 8,6 let.
   - **10. percentil doby zaměstnání** je **5.16 let**. To znamená, že 10 % absolventů opustí svůj obor do 5.16 let od ukončení vzdělání.

Tento výstup naznačuje, že většina absolventů zůstává v oboru relativně dlouho (průměrná doba je přes 8 let), ale je zde také významná část (10 %), která změní obor už po přibližně 5 letech.

