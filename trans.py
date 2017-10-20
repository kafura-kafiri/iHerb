dictionary = {
    '               string With "punctuation" inside of it! Does this work? I hope so.': 'بابا',

    'Quick Links': 'دسترسی سریع',
    'Daily Deal': 'پیشنهاد روزانه',
    'Order History': 'تاریخ جستجوها',
    'Wish List': 'لیست علایق',
    'Contact Us': 'تماس باما',
    'Trending Searches': 'جستجوهای مورد علاقه',
    'Probiotics': 'پروبیوتیک ها',
    'Collagen': 'کلاژن',
    'Search History': 'پیشینه جستجوها',
    'Clear Search History': 'حذف پیشینه',

    'Read More&nbsp;&raquo;': '',
    ''' &copy; Copyright 1997-2017 iHerb Inc. All rights reserved.
                  iHerb&reg; is a registered trademark of iHerb, Inc. Trusted Brands. Healthy Rewards.
                  and the iHerb.com Trusted Brands. Healthy Rewards. Logo are trademarks of iHerb,
                  Inc. *Disclaimer: Statements made, or products sold through this
                  website, have not been evaluated by the United States Food and Drug Administration. They are not
                  intended to diagnose, treat, cure or prevent any disease.''':
        '''''',
    'Learn more': 'بیشتر بدانید',
    'Give 5% &amp; Get 5%': '۵٪ بدهید ۵٪ بگیرید',
    'Get Help Now &raquo;': 'الان کمک بگیرید',
    'Find answers from our knowledge base.': 'جواب خود را از پایگاه داده ما بگیرید.',
    'Ask a Question': 'سوالی بپرسید',
    'CONNECT WITH US': 'باما تماس بگیرید',
    'MOBILE APPS': 'اپلیکیشنها',
    'Supply Chains Act': 'زنجیرهای تامین',
    'Terms of Use': 'شرایط استفاده',
    'Privacy Policy': 'سیاست حفظ حریم خصوصی',
    'Contact Us': 'تماس با ما',
    'Customer Service': 'خدمات مشتری',
    'Healthy Links': 'پیوندهای سالم',
    'My Doloka Page': 'دولوکای من',
    'Doloka Blog': 'بلاگ دولوکا',
    'Doloka RESOURCES': 'منابع دولوکا',
    'Suppliers': 'تامین کنندگان',
    'Careers': 'دستاندرکاران',
    'Promote doloka': 'ترویج ما',
    'We Give Back': 'ماباز میدهیم',
    'About Us': 'درباره ما',
    'ABOUT Doloka': 'درباره دولکا',
    '': '',

    'trending now': 'داغ ترین ها',
    'Best Selling': 'پرفروشا',
    'The biggest gainers in iHerb.com sales rank over the past 24 hours.': 'بیشترین کالاهایی که در ۲۴ ساعت اخیر به فروش رفته اند.',
    'Supplements': 'مکمل ها',
    'Herbs': 'داروهای گیاهی',
    'Bath': 'شستشو',
    'Beauty': 'زیبایی',
    'Grocery': 'خواربار',
    'Baby': 'کودک',
    'Sports': 'ورزشی',
    'Home': 'خانه',
    'Pets': 'حیوانات خانگی',
    'SEE ALL': 'مشاهده همه',
    'Image Coming Soon': 'تصویر در حال بارگذاری',
    'iHerb.com - Vitamins, Supplements &amp; Natural Health Products': 'دولوکا - ویتامین ها مکمل ها و طبیعیجات',
    'Live': 'زنده',
    'doloka': 'دولوکا',
    'Check out what others are buying in real time!': 'محصولاتی که توسط هم میهنان تهیه میشود را به طور آنلاین چک کنید!'

    ''
}


def simplify(phrase):
    import string
    translator = str.maketrans('', '', string.punctuation)
    return phrase.translate(translator).lower().strip()


def trans(phrase):
    phrase = simplify(phrase)
    if phrase in dictionary:
        return dictionary[phrase]
    return phrase


def update():
    _dic = {}
    for k, v in dictionary.items():
        _dic[simplify(k)] = v
    dictionary.clear()
    dictionary.update(_dic)
