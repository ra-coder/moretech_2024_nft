_1. Цифровой профиль для сертификатов и наград:
Платформа должна поддерживать создание и управление цифровым профилем сотрудника, в котором будет храниться
информация о навыках, дипломах, сертификатах, достижениях и рекомендациях для конкретного сотрудника._

- [x] Профилем является стандартный криптокошелек. Можно взять любой в любой текущей сети, или поднять корпоративный блокчейн.
Мы в рамках хакатона использовали Polygon MATIC [polygon.technology]. Выбор на него пал из-за низкой комисии на гад для
создания и выпуска NFT.

- [x] Пример отображения профиля на сайте можно посмотреть тут  
https://iktomi.pro/user-nfts?user_id=3
(Это реальные NFTи реальные кошельки, можете проверить что токен там есть в любом привычном вамм вьюере/ресурсе)

_2. Управление сертификатами:
На платформе должна быть возможность выпуска сертификатов или наград для конкретного сотрудника. После выпуска
сертификат попадает в цифровой профиль.
В случае внешних сервисов или организаций сотрудник может самостоятельно запросить создание сертификата.
В решении должны быть реализованы механизмы выпуска, передачи и отзыва сертификатов._

- [x] Для v0 решения мы отталкивались от выпуска NFT на https://mirror.xyz/ в частности выпустили вот такую коллекцию
https://mirror.xyz/0xb39d9C554EfDea3382D833c7F2E2dc555D08aB82/nft/0x1c0fc9F1AbCf28ca5BB36CC010CCF500459998f2/0
В ближайшей верси надо сделать (повторить и модифицировать функционал mirror.xyz)

- [ ] выпуск "рекомендации" (aka отзвы или коммент) от одного человека другому (NFT)
- [ ] выпуск "коллекции сертификатов/дипломов"
    - [ ] безсрочных
    - [ ] действительных до оперделенной даты
    - [ ] с возможностью аннулирования

- [ ] верефикация организаций (FYC) и (и администрирование ее сотрудников) для пометки от нас что эти сертификаты "
  проверены"

_3. Уникальный NFT:
Платформа должна иметь возможность преобразовывать каждое достижение, сертификат или награду в уникальный NFT._

- [ ] пока не сделано (см пункт выше)


_4. Рекомендации и подтверждения:
   Платформа должна позволять сотрудникам запрашивать и получать рекомендации от коллег, которые будут сохраняться в их
   профилях и могут быть использованы для дальнейшего карьерного роста. Например, можно оставить отзыв о коллеге, с
   которым работал на проекте или подтвердить наличие какого-то навыка._

- [ ] надо сделать реестр навыков (админку его пополнения)
- [ ] голосовалку (оценку) за навык у коллеги с бальной системой (каждый голос - как NFT)

- [ ] API запроса рекомендаций у коллег (???) черещз чат на сайте ???

_5. Система верификации:
Платформа предоставляет возможность верификации данных профиля, таких как дипломы и сертификаты._

- [ ] по каждому NFT надо иметь возможность перейти в профиль, который его выдал (от имени которого был контракт???)
- [ ] в профилях должна быть KYC 
  - [ ] сейчас это частично сделано через привязку через OAuth vk + github
    (задумка в том, что можно подключить аналочно oAuth организации или доменную авторизацию в организации)
  