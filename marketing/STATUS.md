# Стан і межі бази — 2026-11-05

- Базовий готовий кіт: **2026-10-20**, точна копія папки, яку власник надав у цьому завданні. Це обрана основа для подальших змін, а не нове підтвердження здачі в друк.
- **23 макети документів:** 16 попередніх ASP/PSP + 7 Commercial/PGP. Останні 7 = 6 основних документів і окрема обкладинка, разом 27 сторінок. Print/Fillable, прев’ю й варіанти логотипа не рахувати новими макетами.
- Історична перевірка переносного проєкту від 20 жовтня зафіксована в source/06_Release_Data/BUILD_VERIFICATION.txt: 27 сторінок, 456 полів, тексти й пробне заповнення. Це історичний результат, а не новий повний render-тест під час імпорту в Git.
- Під час імпорту перевіряються контрольні суми вихідних файлів і випуску та відсутність заповнених клієнтських значень у PDF-формах. Документи не перебудовуються й не редизайняться.
- Презентації Organization Chart, Contents Track Training, ContentsTrack Overview та три Thank You флаєри **не входять до цього кіта**. Власник не хотів додавати їх до цього пакування.
- Пробні/поточні правки ERP Property Management і PM Brochure від 5 листопада **не включені в готові файли й джерела цього базового випуску**. Перероблений без запиту дизайн не є затвердженим варіантом.

## Поточне окреме звернення колеги — ще не випуск

**Новий тест за репозиторієм, 2026-11-05:** власник вказав Agency EPR Flyer; підготовлено [окремий ERP Property Management review](reviews/2026-11-05-erp-property-management/README.md) із повним наданим абзацом, адаптованими страховими текстами, редагованим copy.json і переносним інструментом. Після зміни перевірено текст, відсутність виходу за текстові блоки й незмінність решти artwork: піксельно ідентичне поза областями замінених текстів при 144 dpi. Фото не додавалось, бо цей ERP-макет не має фотоблоку. Основний випуск не замінено; погодження огляду ще не отримано.

1. **ERP Program flyer:** переорієнтувати страховий напрям на Property Management Solution за наданим колегою текстом. Зберегти існуючий дизайн; поточний файл слід зіставити з каталогом, а не автоматично вважати старий реліз точно тим самим вкладенням.
2. **PM Brochure:** після пошуку власник підтвердив **Commercial Leave Behind Trifold** як потрібний документ. Підготовлено [концепт обкладинки без фото](reviews/2026-11-05-pm-trifold-water-cover/README.md): “WATER DAMAGE? GCPRO HAS YOU COVERED.” та “WATER MITIGATION & RESTORATION”. Дизайн і внутрішні сторінки збережено, фотоблок тимчасово порожній. Фото затопленої квартири/поверху ще обирається; концепт не є новим затвердженим випуском. Випадковий локальний GCPRO_Property_Managers_Flyer.pdf не використовувати замість підтвердженого макета.

Наданий текст для ERP (контент завдання, не дозвіл на новий дизайн):

> For Commercial, Industrial, Senior Living, and Multifamily property management teams, an emergency can disrupt operations, displace residents, and create unbudgeted expenses. GCPro’s FREE Emergency Response Program (ERP) helps your team prepare before a loss occurs and respond with confidence when it does. With a property-specific response plan, an emergency application customized to your staff’s needs, and 24/7 mitigation and full restoration support, GCPro helps simplify after-hours emergencies, limit damage, and return affected spaces to service faster. From protecting business continuity to supporting resident comfort and retention, our goal is to reduce disruption, control unexpected costs, and help protect your net operating income (NOI).

Обговорювалася майбутня сторінка/розділ сайту для програм і матеріалів. Зміст і подача потребують думок команди; затвердженої структури/публікації в цьому маркетинговому кітi немає.
