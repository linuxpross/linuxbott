import telebot
from telebot import types

TOKEN = '6956484987:AAFRoR8EdupQXkhkR7B5e0erA1o7v4qiiDA'

bot = telebot.TeleBot(TOKEN)

histori = (
    'Корни Linux прослеживаются ещё с 70-х годов 20-го века. Точкой отсчёта можно считать появление операционной системы Unix в 1969-м году в США в фирме Bell Laboratories, дочернем подразделении компании AT&T. Unix стала основной для большого количества операционных систем промышленного класса. Самые основные из них отображены на этой временной шкале:'
)
linux_admin = [
    'Системный администратор Linux (или администратор Unix-подобных систем) - это специалист по управлению, обслуживанию и поддержке операционных систем на базе ядра Linux. Их задачи могут включать в себя установку, настройку, обновление и обслуживание операционной системы, управление пользователями и правами доступа, мониторинг производительности, а также решение проблем, связанных с работой серверов и сетевых сервисов.'
    'Основные обязанности системного администратора Linux могут варьироваться в зависимости от конкретных требований и масштаба организации, в которой он работает. Однако, в общем, их работа связана с обеспечением стабильной и безопасной работы серверов, сетей и других системных ресурсов на базе Linux.'
    'Навыки системного администратора Linux могут включать в себя знание командной строки, опыт работы с различными дистрибутивами Linux, умение настраивать и обслуживать сетевые службы, а также знание принципов безопасности информационных систем.'
    'хотите ли стать ситемним админом ??'
]
video_yes_admin = [
    'Получите базовое образование в области информационных технологий, компьютерных наук или смежной области. Освойте основы операционных систем, сетей, и компьютерной безопасности.Опыт работы и стажировки:'
    'Получите опыт работы в области информационных технологий. Начните с поддержки пользователей, чтобы понять основы работы с системами.Работайте над проектами, связанными с Linux, чтобы получить опыт работы с этой операционной системой.Рассматривайте возможность стажировок или волонтёрской работы в компаниях, использующих Linux.Сертификации:'
    'Получите опыт работы в области информационных технологий. Начните с поддержки пользователей, чтобы понять основы работы с системами.Работайте над проектами, связанными с Linux, чтобы получить опыт работы с этой операционной системой.Рассматривайте возможность стажировок или волонтёрской работы в компаниях, использующих Linux.Сертификации:'
    'Получение сертификаций может укрепить ваши навыки и повысить вашу привлекательность для работодателей. Некоторые из популярных сертификаций для системных администраторов Linux включают:CompTIA Linux+Red Hat Certified Engineer (RHCE)LPIC (Linux Professional Institute Certification)Самообразование:'
    'Изучайте Linux на практике. Установите различные дистрибутивы, настраивайте их, работайте с командной строкой.Изучайте скриптовые языки, такие как Bash, для автоматизации рутинных задач.Следите за сообществами и ресурсами Linux, такими как форумы, блоги, и ресурсы вроде Stack Overflow.Постоянное обучение:Поля информационных технологий постоянно развиваются. Следите за новыми тенденциями, технологиями и инструментами.Создайте свой профиль:Создайте профиль на платформах профессионального общения, таких как LinkedIn, чтобы делиться своим опытом и находить новые возможности.Навыки общения:Развивайте свои навыки общения, так как системные администраторы часто взаимодействуют с другими членами команды и пользователями.Поиск работы:Ищите вакансии и применяйтесь на позиции системного администратора Linux. Работайте над составлением качественного резюме и сопроводительного письма.'
]





photo_linux = 'linux1.jpg'
ubuntu_linux = 'Ubuntu: Один из наиболее популярных и широко используемых дистрибутивов с акцентом на простоте использования'
debian_linux = 'Debian: Debian является основой для многих других дистрибутивов и славится своей стабильностью и сильной философией свободного программного обеспечения.'
fedora_linux = 'Fedora: Разработанная и поддерживаемая сообществом, Fedora является инновационным дистрибутивом с недавними версиями программного обеспечения.'
arch_linux = 'Arch Linux: Основная особенность Arch Linux - это его простота и полная настраиваемость. Arch Linux предоставляет пользователям полный контроль над системой.'
opensuse_linux = 'openSUSE: Разработанный и поддерживаемый компанией SUSE, openSUSE предоставляет различные редакции, такие как openSUSE Leap и openSUSE Tumbleweed.'
centos_linux = 'CentOS: Основанная на исходном коде Red Hat Enterprise Linux (RHEL), CentOS предоставляет стабильную и бесплатную альтернативу RHEL.'
mint_linux = 'Mint: Ориентированный на начинающих пользователей, Linux Mint основан на Ubuntu и предоставляет дружественный интерфейс пользователя.'
gentoo_linux = 'Gentoo: Gentoo является дистрибутивом, в котором пользователи компилируют большинство программного обеспечения с исходного кода. Он ориентирован на опытных пользователей.'
slackware_linux = 'Slackware: Один из старейших дистрибутивов Linux, Slackware придерживается простоты и минимализма.'
kali_linux = 'Kali Linux: Ориентированный на тестирование на проникновение и безопасность, Kali Linux предоставляет инструменты для проверки безопасности и тестирования на проникновение.'
video_linux  = 'video1.mp4'
@bot.message_handler(commands=['start'])
def send_start_message(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Linux", callback_data='Linux')
    markup.add(button1)

    with open(photo_linux, 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo, caption='Всем привет! Этот бот - телеграм-бот про Linux. Здесь есть инструменты и обучающие материалы.', reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_message(message):
    bot.send_message(message.chat.id, 'По всем вопросам пишите разработчику https://t.me/Argishti2007')

@bot.callback_query_handler(func=lambda call: True)
def calbax_button(call):
    if call.data == 'Linux':
        markup = types.InlineKeyboardMarkup()
        butt1 = types.InlineKeyboardButton("История", callback_data='история')
        butt2 = types.InlineKeyboardButton("Дистрибутивы", callback_data='дистрибутивы')
        butt3 = types.InlineKeyboardButton("Сис админ Linux", callback_data='сис админ Linux')
        butt4 = types.InlineKeyboardButton("DEV OPS", callback_data='DEV OPS')
        markup.add(butt1, butt2, butt3, butt4)
        bot.send_message(call.message.chat.id, 'Привет! Какая информация вас интересует про Linux?', reply_markup=markup)
    
    elif call.data == 'история':
        bot.send_message(call.message.chat.id, histori)
    
    elif call.data == 'дистрибутивы':
        markup = types.InlineKeyboardMarkup()
        ubuntu1 = types.InlineKeyboardButton("Ubuntu", callback_data='Ubuntu')
        debian = types.InlineKeyboardButton("Debian", callback_data='Debian')
        fedora = types.InlineKeyboardButton("Fedora", callback_data='Fedora')
        arch_linux = types.InlineKeyboardButton("Arch Linux", callback_data='Arch Linux')
        opensuse = types.InlineKeyboardButton("openSUSE", callback_data='openSUSE')
        mint_linux = types.InlineKeyboardButton("Mint", callback_data='Mint')
        centos_linux = types.InlineKeyboardButton("CentOS", callback_data='CentOS')
        gentoo = types.InlineKeyboardButton("Gentoo", callback_data='Gentoo')
        slack_linux = types.InlineKeyboardButton("Slack", callback_data='Slack')
        kali_linux = types.InlineKeyboardButton("Kali", callback_data='Kali')
        markup.add(ubuntu1, debian, fedora, arch_linux, opensuse, mint_linux, centos_linux, gentoo, slack_linux, kali_linux)
        bot.send_message(call.message.chat.id, 'Выберите дистрибутив:', reply_markup=markup)

    # Добавлены исправления для кнопок дистрибутивов
    elif call.data == 'Ubuntu':
        markup_ubuntu = types.InlineKeyboardMarkup()
        ubuntu11 = types.InlineKeyboardButton("Ubuntu", callback_data='Ubuntu')
        debian1 = types.InlineKeyboardButton("Debian", callback_data='Debian')
        fedora1 = types.InlineKeyboardButton("Fedora", callback_data='Fedora')
        arch_linux1 = types.InlineKeyboardButton("Arch Linux", callback_data='Arch Linux')
        opensuse1 = types.InlineKeyboardButton("openSUSE", callback_data='openSUSE')
        mint_linux1 = types.InlineKeyboardButton("Mint", callback_data='Mint')
        centos_linux1 = types.InlineKeyboardButton("CentOS", callback_data='CentOS')
        gentoo1 = types.InlineKeyboardButton("Gentoo", callback_data='Gentoo')
        slack_linux1 = types.InlineKeyboardButton("Slack", callback_data='Slack')
        kali_linux1 = types.InlineKeyboardButton("Kali", callback_data='Kali')
        ubuntu_iso1 = types.InlineKeyboardButton("ISO DOWNLOADS", callback_data='ISO DOWNLOADS')
        markup_ubuntu.add(debian1,fedora1,ubuntu11,arch_linux1,mint_linux1,opensuse1,centos_linux1,gentoo1,slack_linux1,kali_linux1,ubuntu_iso1)
        with open('ubuntu.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo=photo, caption=ubuntu_linux, reply_markup=markup_ubuntu)

    elif call.data == 'Debian':
        markup_debian = types.InlineKeyboardMarkup()
        ubuntu12 = types.InlineKeyboardButton("Ubuntu", callback_data='Ubuntu')
        debian2 = types.InlineKeyboardButton("Debian", callback_data='Debian')
        fedora2 = types.InlineKeyboardButton("Fedora", callback_data='Fedora')
        arch_linux2 = types.InlineKeyboardButton("Arch Linux", callback_data='Arch Linux')
        opensuse2 = types.InlineKeyboardButton("openSUSE", callback_data='openSUSE')
        mint_linux2 = types.InlineKeyboardButton("Mint", callback_data='Mint')
        centos_linux2 = types.InlineKeyboardButton("CentOS", callback_data='CentOS')
        gentoo2 = types.InlineKeyboardButton("Gentoo", callback_data='Gentoo')
        slack_linux2 = types.InlineKeyboardButton("Slack", callback_data='Slack')
        kali_linux2 = types.InlineKeyboardButton("Kali", callback_data='Kali')
        debian_iso = types.InlineKeyboardButton("ISO DOWNLOADS", callback_data='ISO DOWNLOADS')
        markup_debian.add(ubuntu12,debian2,fedora2,arch_linux2,opensuse2,mint_linux2,centos_linux2,gentoo2,slack_linux2,kali_linux2,debian_iso)
        with open('debian.jpg', 'rb') as photo2:
            bot.send_photo(call.message.chat.id, photo=photo2, caption=debian_linux, reply_markup=markup_debian)

    elif call.data == 'Fedora':
        markup_fedora = types.InlineKeyboardMarkup()
        ubuntu13 = types.InlineKeyboardButton("Ubuntu", callback_data='Ubuntu')
        debian3 = types.InlineKeyboardButton("Debian", callback_data='Debian')
        fedora3 = types.InlineKeyboardButton("Fedora", callback_data='Fedora')
        arch_linux3 = types.InlineKeyboardButton("Arch Linux", callback_data='Arch Linux')
        opensuse3 = types.InlineKeyboardButton("openSUSE", callback_data='openSUSE')
        mint_linux3 = types.InlineKeyboardButton("Mint", callback_data='Mint')
        centos_linux3 = types.InlineKeyboardButton("CentOS", callback_data='CentOS')
        gentoo3 = types.InlineKeyboardButton("Gentoo", callback_data='Gentoo')
        slack_linux3 = types.InlineKeyboardButton("Slack", callback_data='Slack')
        kali_linux3 = types.InlineKeyboardButton("Kali", callback_data='Kali')
        fedora_iso = types.InlineKeyboardButton("ISO DOWNLOADS", callback_data='ISO DOWNLOADS')
        markup_fedora.add(ubuntu13,debian3,fedora3,arch_linux3,opensuse3,mint_linux3,centos_linux3,gentoo3,slack_linux3,kali_linux3,fedora_iso)
        with open('fedora.jpg','rb') as photo3:
            bot.send_photo(call.message.chat.id,photo=photo3, caption=fedora_linux, reply_markup=markup_fedora)

    elif call.data == 'Arch Linux':
        markup_arch = types.InlineKeyboardMarkup()
        ubuntu14 = types.InlineKeyboardButton("Ubuntu", callback_data='Ubuntu')
        debian4 = types.InlineKeyboardButton("Debian", callback_data='Debian')
        fedora4 = types.InlineKeyboardButton("Fedora", callback_data='Fedora')
        arch_linux4 = types.InlineKeyboardButton("Arch Linux", callback_data='Arch Linux')
        opensuse14 = types.InlineKeyboardButton("openSUSE", callback_data='openSUSE')
        mint_linux4 = types.InlineKeyboardButton("Mint", callback_data='Mint')
        centos_linux4 = types.InlineKeyboardButton("CentOS", callback_data='CentOS')
        gentoo4 = types.InlineKeyboardButton("Gentoo", callback_data='Gentoo')
        slack_linux4 = types.InlineKeyboardButton("Slack", callback_data='Slack')
        kali_linux4 = types.InlineKeyboardButton("Kali", callback_data='Kali')
        arch_iso4 = types.InlineKeyboardButton("ISO DOWNLOADS", callback_data='ISO DOWNLOADS')
        markup_arch.add(ubuntu14,debian4,fedora4,arch_linux4,opensuse14,mint_linux4,centos_linux4,gentoo4,slack_linux4,kali_linux4,arch_iso4)
        with open('Arch.jpg','rb') as photo4:
            bot.send_photo(call.message.chat.id,photo=photo4,caption=arch_linux, reply_markup=markup_arch)

    elif call.data == 'openSUSE':
        markup_opensuse = types.InlineKeyboardMarkup()
        ubuntu15 = types.InlineKeyboardButton("Ubuntu", callback_data='Ubuntu')
        debian5 = types.InlineKeyboardButton("Debian", callback_data='Debian')
        fedora5 = types.InlineKeyboardButton("Fedora", callback_data='Fedora')
        arch_linux5 = types.InlineKeyboardButton("Arch Linux", callback_data='Arch Linux')
        opensuse5 = types.InlineKeyboardButton("openSUSE", callback_data='openSUSE')
        mint_linux5 = types.InlineKeyboardButton("Mint", callback_data='Mint')
        centos_linux5 = types.InlineKeyboardButton("CentOS", callback_data='CentOS')
        gentoo5 = types.InlineKeyboardButton("Gentoo", callback_data='Gentoo')
        slack_linux5 = types.InlineKeyboardButton("Slack", callback_data='Slack')
        kali_linux5 = types.InlineKeyboardButton("Kali", callback_data='Kali')
        opensuse_iso = types.InlineKeyboardButton("ISO DOWNLOADS", callback_data='ISO DOWNLOADS')
        markup_opensuse.add(ubuntu15,debian5,fedora5,arch_linux5,opensuse5,mint_linux5,centos_linux5,gentoo5,slack_linux5,kali_linux5,opensuse_iso)
        with open('openSUSE.png','rb') as photo5:
            bot.send_photo(call.message.chat.id, photo=photo5,caption=opensuse_linux, reply_markup=markup_opensuse)

    elif call.data == 'CentOS':
        markup_centos = types.InlineKeyboardMarkup()
        centos_iso = types.InlineKeyboardButton("ISO DOWNLOADS", callback_data='ISO DOWNLOADS')
        ubuntu16 = types.InlineKeyboardButton("Ubuntu", callback_data='Ubuntu')
        debian6 = types.InlineKeyboardButton("Debian", callback_data='Debian')
        fedora6 = types.InlineKeyboardButton("Fedora", callback_data='Fedora')
        arch_linux6 = types.InlineKeyboardButton("Arch Linux", callback_data='Arch Linux')
        opensuse6 = types.InlineKeyboardButton("openSUSE", callback_data='openSUSE')
        mint_linux6 = types.InlineKeyboardButton("Mint", callback_data='Mint')
        centos_linux6 = types.InlineKeyboardButton("CentOS", callback_data='CentOS')
        gentoo6 = types.InlineKeyboardButton("Gentoo", callback_data='Gentoo')
        slack_linux6 = types.InlineKeyboardButton("Slack", callback_data='Slack')
        kali_linux6 = types.InlineKeyboardButton("Kali", callback_data='Kali')
        markup_centos.add(ubuntu16,debian6,fedora6,arch_linux6,opensuse6,mint_linux6,centos_linux6,gentoo6,slack_linux6,kali_linux6,centos_iso)
        with open('centos.jpg','rb') as photo6:
            bot.send_photo(call.message.chat.id,photo=photo6,caption=centos_linux, reply_markup=markup_centos)

    elif call.data == 'Mint':
        markup_mint = types.InlineKeyboardMarkup()
        mint_iso = types.InlineKeyboardButton("ISO DOWNLOADS", callback_data='ISO DOWNLOADS')
        ubuntu17 = types.InlineKeyboardButton("Ubuntu", callback_data='Ubuntu')
        debian7 = types.InlineKeyboardButton("Debian", callback_data='Debian')
        fedora7 = types.InlineKeyboardButton("Fedora", callback_data='Fedora')
        arch_linux7 = types.InlineKeyboardButton("Arch Linux", callback_data='Arch Linux')
        opensuse7 = types.InlineKeyboardButton("openSUSE", callback_data='openSUSE')
        mint_linux7 = types.InlineKeyboardButton("Mint", callback_data='Mint')
        centos_linux7 = types.InlineKeyboardButton("CentOS", callback_data='CentOS')
        gentoo7 = types.InlineKeyboardButton("Gentoo", callback_data='Gentoo')
        slack_linux7 = types.InlineKeyboardButton("Slack", callback_data='Slack')
        kali_linux7 = types.InlineKeyboardButton("Kali", callback_data='Kali')
        markup_mint.add(ubuntu17,debian7,fedora7,arch_linux7,opensuse7,mint_linux7,centos_linux7,gentoo7,slack_linux7,kali_linux7,mint_iso)

        with open('Mit.jpg','rb') as photo7:
            bot.send_photo(call.message.chat.id,photo=photo7 ,caption=mint_linux, reply_markup=markup_mint)

    elif call.data == 'Gentoo':
        markup_gentoo = types.InlineKeyboardMarkup()
        gentoo_iso = types.InlineKeyboardButton("ISO DOWNLOADS", callback_data='ISO DOWNLOADS')
        ubuntu8 = types.InlineKeyboardButton("Ubuntu", callback_data='Ubuntu')
        debian8 = types.InlineKeyboardButton("Debian", callback_data='Debian')
        fedora8 = types.InlineKeyboardButton("Fedora", callback_data='Fedora')
        arch_linux8 = types.InlineKeyboardButton("Arch Linux", callback_data='Arch Linux')
        opensuse8 = types.InlineKeyboardButton("openSUSE", callback_data='openSUSE')
        mint_linux8 = types.InlineKeyboardButton("Mint", callback_data='Mint')
        centos_linux8 = types.InlineKeyboardButton("CentOS", callback_data='CentOS')
        gentoo8 = types.InlineKeyboardButton("Gentoo", callback_data='Gentoo')
        slack_linux8 = types.InlineKeyboardButton("Slack", callback_data='Slack')
        kali_linux8 = types.InlineKeyboardButton("Kali", callback_data='Kali')
        markup_gentoo.add(ubuntu8,debian8,fedora8,arch_linux8,opensuse8,mint_linux8,centos_linux8,gentoo8,slack_linux8,kali_linux8,gentoo8)
        with open('gentoo.png','rb') as photo8:
            bot.send_photo(call.message.chat.id,photo=photo8, caption=gentoo_linux, reply_markup=markup_gentoo)

    elif call.data == 'Slack':
        markup_slack = types.InlineKeyboardMarkup()
        slack_iso = types.InlineKeyboardButton("ISO DOWNLOADS", callback_data='ISO DOWNLOADS')
        ubuntu19 = types.InlineKeyboardButton("Ubuntu", callback_data='Ubuntu')
        debian9 = types.InlineKeyboardButton("Debian", callback_data='Debian')
        fedora9 = types.InlineKeyboardButton("Fedora", callback_data='Fedora')
        arch_linux9 = types.InlineKeyboardButton("Arch Linux", callback_data='Arch Linux')
        opensuse9 = types.InlineKeyboardButton("openSUSE", callback_data='openSUSE')
        mint_linux9 = types.InlineKeyboardButton("Mint", callback_data='Mint')
        centos_linux9 = types.InlineKeyboardButton("CentOS", callback_data='CentOS')
        gentoo9 = types.InlineKeyboardButton("Gentoo", callback_data='Gentoo')
        slack_linux9 = types.InlineKeyboardButton("Slack", callback_data='Slack')
        kali_linux9 = types.InlineKeyboardButton("Kali", callback_data='Kali')
        markup_slack.add(ubuntu19,debian9,fedora9,arch_linux9,opensuse9,mint_linux9,centos_linux9,gentoo9,slack_linux9,kali_linux9,slack_iso)
        with open('slack.png','rb') as photo9:
            bot.send_photo(call.message.chat.id,photo=photo9,caption=slackware_linux, reply_markup=markup_slack)

    elif call.data == 'Kali':
        markup_kali = types.InlineKeyboardMarkup()
        kali_iso = types.InlineKeyboardButton("ISO DOWNLOADS", callback_data='ISO DOWNLOADS')
        ubuntu20 = types.InlineKeyboardButton("Ubuntu", callback_data='Ubuntu')
        debian10 = types.InlineKeyboardButton("Debian", callback_data='Debian')
        fedora10 = types.InlineKeyboardButton("Fedora", callback_data='Fedora')
        arch_linux10 = types.InlineKeyboardButton("Arch Linux", callback_data='Arch Linux')
        opensuse10 = types.InlineKeyboardButton("openSUSE", callback_data='openSUSE')
        mint_linux10 = types.InlineKeyboardButton("Mint", callback_data='Mint')
        centos_linux10 = types.InlineKeyboardButton("CentOS", callback_data='CentOS')
        gentoo10 = types.InlineKeyboardButton("Gentoo", callback_data='Gentoo')
        slack_linux10 = types.InlineKeyboardButton("Slack", callback_data='Slack')
        kali_linux10 = types.InlineKeyboardButton("Kali", callback_data='Kali')
        markup_kali.add(ubuntu20,debian10,fedora10,arch_linux10,opensuse10,mint_linux10,centos_linux10,gentoo10,slack_linux10,kali_linux10,kali_iso)
        with open('kali.png','rb') as photo10:
            bot.send_photo(call.message.chat.id,photo=photo10, caption=kali_linux, reply_markup=markup_kali)

    elif call.data == 'ISO DOWNLOADS':
        markup_iso = types.InlineKeyboardMarkup()
        ubuntu21 = types.InlineKeyboardButton("Ubuntu", callback_data='Ubuntu')
        debian11 = types.InlineKeyboardButton("Debian", callback_data='Debian')
        fedora11 = types.InlineKeyboardButton("Fedora", callback_data='Fedora')
        arch_linux11 = types.InlineKeyboardButton("Arch Linux", callback_data='Arch Linux')
        opensuse11 = types.InlineKeyboardButton("openSUSE", callback_data='openSUSE')
        mint_linux11 = types.InlineKeyboardButton("Mint", callback_data='Mint')
        centos_linux11 = types.InlineKeyboardButton("CentOS", callback_data='CentOS')
        gentoo11 = types.InlineKeyboardButton("Gentoo", callback_data='Gentoo')
        slack_linux11 = types.InlineKeyboardButton("Slack", callback_data='Slack')
        kali_linux11 = types.InlineKeyboardButton("Kali", callback_data='Kali')
        markup_iso.add(ubuntu21,debian11,fedora11,arch_linux11,opensuse11,mint_linux11,centos_linux11,gentoo11,slack_linux11,kali_linux11)
        with open('iso.jpg','rb') as photo11:
            bot.send_photo(call.message.chat.id,photo=photo11,caption='Выберите дистрибутив для загрузки', reply_markup=markup_iso)
        
    elif call.data == 'сис админ Linux':
        markup_sysadmin = types.InlineKeyboardMarkup()
        sysadmin_yes = types.InlineKeyboardButton("да",callback_data="да")
        sysadmin_no = types.InlineKeyboardButton("нет ",callback_data="нет")
        markup_sysadmin.add(sysadmin_yes,sysadmin_no)
        bot.send_message(call.message.chat.id,linux_admin,reply_markup=markup_sysadmin)
     
    elif call.data == 'да':
        with open(video_linux ,'rb') as video1:
            user_id = call.message.chat.id
            bot.send_video(user_id,video1,)
            bot.send_message(call.message.chat.id,video_yes_admin)

if __name__ == '__main__':
    bot.polling(none_stop=True)
