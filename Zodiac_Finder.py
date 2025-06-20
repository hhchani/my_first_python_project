import time
import streamlit as st

# Zodiac data with emojis and personality traits
zodiac_data = {
    "Capricorn": {
        "emoji": "♑",
        "traits": {
            "English": ["Ambitious", "Disciplined", "Patient", "Practical", "Responsible"],
            "Indonesian": ["Ambisius", "Disiplin", "Sabar", "Praktis", "Bertanggung jawab"],
            "Spanish": ["Ambicioso", "Disciplinado", "Paciente", "Práctico", "Responsable"],
            "French": ["Ambitieux", "Discipliné", "Patient", "Pratique", "Responsable"],
            "German": ["Ehrgeizig", "Diszipliniert", "Geduldig", "Pragmatisch", "Verantwortungsbewusst"],
            "Portuguese": ["Ambicioso", "Disciplinado", "Paciente", "Prático", "Responsável"],
            "Hindi": ["महत्वाकांक्षी", "अनुशासित", "धैर्यवान", "व्यावहारिक", "जिम्मेदार"],
            "Japanese": ["野心的", "規律正しい", "忍耐強い", "実用的", "責任感が強い"],
            "Russian": ["Амбициозный", "Дисциплинированный", "Терпеливый", "Практичный", "Ответственный"],
            "Chinese": ["雄心勃勃", "纪律严明", "耐心", "务实", "负责任"],
            "Arabic": ["طموح", "منضبط", "صبور", "عملي", "مسؤول"]
        },
        "description": {
            "English": "Capricorns are known for their determination and strong work ethic. They value structure and tradition.",
            "Indonesian": "Capricorn dikenal dengan tekad dan etos kerja yang kuat. Mereka menghargai struktur dan tradisi.",
            "Spanish": "Los Capricornio son conocidos por su determinación y fuerte ética de trabajo. Valoran la estructura y la tradición.",
            "French": "Les Capricornes sont connus pour leur détermination et leur forte éthique de travail. Ils valorisent la structure et la tradition.",
            "German": "Steinböcke sind für ihre Entschlossenheit und starke Arbeitsmoral bekannt. Sie schätzen Struktur und Tradition.",
            "Portuguese": "Capricornianos são conhecidos por sua determinação e forte ética de trabalho. Eles valorizam estrutura e tradição.",
            "Hindi": "मकर राशि वाले अपने दृढ़ संकल्प और मजबूत कार्य नीति के लिए जाने जाते हैं। वे संरचना और परंपरा को महत्व देते हैं।",
            "Japanese": "山羊座は決断力と強い職業倫理で知られています。彼らは構造と伝統を重視します。",
            "Russian": "Козероги известны своей решимостью и сильной трудовой этикой. Они ценят структуру и традиции.",
            "Chinese": "摩羯座以决心和强烈的职业道德而闻名。他们重视结构和传统。",
            "Arabic": "معروف عن الجدي عزمه وأخلاقيات العمل القوية. يقدرون البنية والتقاليد."
        }
    },
    "Aquarius": {
        "emoji": "♒",
        "traits": {
            "English": ["Innovative", "Humanitarian", "Independent", "Intellectual", "Unconventional"],
            "Indonesian": ["Inovatif", "Humanis", "Mandiri", "Intelektual", "Nonkonvensional"],
            "Spanish": ["Innovador", "Humanitario", "Independiente", "Intelectual", "Poco convencional"],
            "French": ["Innovant", "Humanitaire", "Indépendant", "Intellectuel", "Non conventionnel"],
            "German": ["Innovativ", "Humanitär", "Unabhängig", "Intellektuell", "Unkonventionell"],
            "Portuguese": ["Inovador", "Humanitário", "Independente", "Intelectual", "Não convencional"],
            "Hindi": ["नवीन", "मानवतावादी", "स्वतंत्र", "बौद्धिक", "अपरंपरागत"],
            "Japanese": ["革新的", "人道主義", "独立心が強い", "知的", "型破り"],
            "Russian": ["Инновационный", "Гуманитарный", "Независимый", "Интеллектуальный", "Нетрадиционный"],
            "Chinese": ["创新", "人道主义", "独立", "知识分子", "非常规"],
            "Arabic": ["مبتكر", "إنساني", "مستقل", "فكري", "غير تقليدي"]
        },
        "description": {
            "English": "Aquarians are forward-thinking and value their independence. They're often drawn to humanitarian causes.",
            "Indonesian": "Aquarius berpikiran maju dan menghargai kemandirian. Mereka sering tertarik pada tujuan kemanusiaan.",
            "Spanish": "Los Acuario son progresistas y valoran su independencia. A menudo se sienten atraídos por causas humanitarias.",
            "French": "Les Verseaux sont avant-gardistes et valorisent leur indépendance. Ils sont souvent attirés par les causes humanitaires.",
            "German": "Wassermänner sind vorausschauend und schätzen ihre Unabhängigkeit. Sie fühlen sich oft zu humanitären Anliegen hingezogen.",
            "Portuguese": "Aquarianos são visionários e valorizam sua independência. Eles são frequentemente atraídos por causas humanitárias.",
            "Hindi": "कुंभ राशि वाले आगे की सोच वाले होते हैं और अपनी स्वतंत्रता को महत्व देते हैं। वे अक्सर मानवीय कारणों से आकर्षित होते हैं।",
            "Japanese": "水瓶座は先見の明があり、自立を重視します。彼らはよく人道的な活動に引き寄せられます。",
            "Russian": "Водолеи прогрессивны и ценят свою независимость. Их часто привлекают гуманитарные цели.",
            "Chinese": "水瓶座具有前瞻性思维，重视独立性。他们经常被人道主义事业所吸引。",
            "Arabic": "الدلو متقدمون في التفكير ويقدرون استقلاليتهم. غالبًا ما ينجذبون إلى القضايا الإنسانية."
        }
    },
    "Pisces": {
        "emoji": "♓",
        "traits": {
            "English": ["Compassionate", "Artistic", "Intuitive", "Gentle", "Wise"],
            "Indonesian": ["Penuh kasih", "Artistik", "Intuitif", "Lembut", "Bijaksana"],
            "Spanish": ["Compasivo", "Artístico", "Intuitivo", "Gentil", "Sabio"],
            "French": ["Compatissant", "Artistique", "Intuitif", "Doux", "Sage"],
            "German": ["Mitfühlend", "Künstlerisch", "Intuitiv", "Sanft", "Weise"],
            "Portuguese": ["Compassivo", "Artístico", "Intuitivo", "Gentil", "Sábio"],
            "Hindi": ["दयालु", "कलात्मक", "सहजज्ञ", "कोमल", "बुद्धिमान"],
            "Japanese": ["思いやりがある", "芸術的", "直感的", "優しい", "賢い"],
            "Russian": ["Сочувствующий", "Творческий", "Интуитивный", "Мягкий", "Мудрый"],
            "Chinese": ["富有同情心", "艺术", "直觉", "温柔", "明智"],
            "Arabic": ["رحيم", "فني", "بديهي", "لطيف", "حكيم"]
        },
        "description": {
            "English": "Pisces are deeply intuitive and often artistic. They're compassionate and sensitive to others' emotions.",
            "Indonesian": "Pisces sangat intuitif dan seringkali artistik. Mereka penuh kasih dan peka terhadap emosi orang lain.",
            "Spanish": "Los Piscis son profundamente intuitivos y a menudo artísticos. Son compasivos y sensibles a las emociones de los demás.",
            "French": "Les Poissons sont profondément intuitifs et souvent artistiques. Ils sont compatissants et sensibles aux émotions des autres.",
            "German": "Fische sind zutiefst intuitiv und oft künstlerisch veranlagt. Sie sind mitfühlend und sensibel für die Gefühle anderer.",
            "Portuguese": "Peixes são profundamente intuitivos e muitas vezes artísticos. Eles são compassivos e sensíveis às emoções dos outros.",
            "Hindi": "मीन राशि वाले गहराई से सहजज्ञ और अक्सर कलात्मक होते हैं। वे दयालु होते हैं और दूसरों की भावनाओं के प्रति संवेदनशील होते हैं।",
            "Japanese": "魚座は非常に直感的で、芸術的であることが多いです。彼らは思いやりがあり、他人の感情に敏感です。",
            "Russian": "Рыбы глубоко интуитивны и часто обладают творческими способностями. Они сострадательны и чувствительны к эмоциям других.",
            "Chinese": "双鱼座具有深刻的直觉，通常具有艺术气息。他们富有同情心，对他人的情绪敏感。",
            "Arabic": "الحوت بديهي للغاية وغالبًا ما يكون فنيًا. إنهم رحماء وحساسون لمشاعر الآخرين."
        }
    },
    "Aries": {
        "emoji": "♈",
        "traits": {
            "English": ["Courageous", "Energetic", "Optimistic", "Honest", "Passionate"],
            "Indonesian": ["Berani", "Enerjik", "Optimis", "Jujur", "Bersemangat"],
            "Spanish": ["Valiente", "Energético", "Optimista", "Honesto", "Apasionado"],
            "French": ["Courageux", "Énergique", "Optimiste", "Honnête", "Passionné"],
            "German": ["Mutig", "Energisch", "Optimistisch", "Ehrlich", "Leidenschaftlich"],
            "Portuguese": ["Corajoso", "Energético", "Otimista", "Honesto", "Apaixonado"],
            "Hindi": ["साहसी", "ऊर्जावान", "आशावादी", "ईमानदार", "जुनूनी"],
            "Japanese": ["勇敢", "エネルギッシュ", "楽観的", "正直", "情熱的"],
            "Russian": ["Храбрый", "Энергичный", "Оптимистичный", "Честный", "Страстный"],
            "Chinese": ["勇敢", "精力充沛", "乐观", "诚实", "热情"],
            "Arabic": ["شجاع", "نشيط", "متفائل", "صادق", "شغوف"]
        },
        "description": {
            "English": "Aries are bold and ambitious. They're natural leaders with lots of energy and enthusiasm.",
            "Indonesian": "Aries berani dan ambisius. Mereka adalah pemimpin alami dengan banyak energi dan antusiasme.",
            "Spanish": "Los Aries son audaces y ambiciosos. Son líderes naturales con mucha energía y entusiasmo.",
            "French": "Les Bélier sont audacieux et ambitieux. Ce sont des leaders naturels avec beaucoup d'énergie et d'enthousiasme.",
            "German": "Widder sind mutig und ehrgeizig. Sie sind geborene Anführer mit viel Energie und Enthusiasmus.",
            "Portuguese": "Áries são corajosos e ambiciosos. Eles são líderes naturais com muita energia e entusiasmo.",
            "Hindi": "मेष राशि वाले साहसी और महत्वाकांक्षी होते हैं। वे प्राकृतिक नेता होते हैं जिनमें बहुत ऊर्जा और उत्साह होता है।",
            "Japanese": "牡羊座は大胆で野心的です。彼らは多くのエネルギーと熱意を持った生まれながらのリーダーです。",
            "Russian": "Овны смелы и амбициозны. Они прирожденные лидеры с большим запасом энергии и энтузиазма.",
            "Chinese": "白羊座大胆而雄心勃勃。他们是天生的领导者，充满活力和热情。",
            "Arabic": "الحمل جريء وطموح. هم قادة بالفطرة يتمتعون بالكثير من الطاقة والحماس."
        }
    },
    "Taurus": {
        "emoji": "♉",
        "traits": {
            "English": ["Reliable", "Patient", "Practical", "Devoted", "Responsible"],
            "Indonesian": ["Dapat diandalkan", "Sabar", "Praktis", "Setia", "Bertanggung jawab"],
            "Spanish": ["Confiable", "Paciente", "Práctico", "Dedicado", "Responsable"],
            "French": ["Fiable", "Patient", "Pratique", "Dévoué", "Responsable"],
            "German": ["Zuverlässig", "Geduldig", "Pragmatisch", "Hingebungsvoll", "Verantwortungsbewusst"],
            "Portuguese": ["Confiável", "Paciente", "Prático", "Dedicado", "Responsável"],
            "Hindi": ["भरोसेमंद", "धैर्यवान", "व्यावहारिक", "समर्पित", "जिम्मेदार"],
            "Japanese": ["信頼できる", "忍耐強い", "実用的", "献身的", "責任感が強い"],
            "Russian": ["Надежный", "Терпеливый", "Практичный", "Преданный", "Ответственный"],
            "Chinese": ["可靠", "耐心", "务实", "忠诚", "负责任"],
            "Arabic": ["موثوق", "صبور", "عملي", "مخلص", "مسؤول"]
        },
        "description": {
            "English": "Taurus values stability and comfort. They're reliable and persistent once they set their mind to something.",
            "Indonesian": "Taurus menghargai stabilitas dan kenyamanan. Mereka dapat diandalkan dan gigih begitu mereka memutuskan sesuatu.",
            "Spanish": "Tauro valora la estabilidad y la comodidad. Son confiables y persistentes una vez que se proponen algo.",
            "French": "Le Taureau valorise la stabilité et le confort. Ils sont fiables et persévérants une fois qu'ils ont décidé quelque chose.",
            "German": "Stiere schätzen Stabilität und Komfort. Sie sont zuverlässig und beharrlich, wenn sie sich etwas in den Kopf gesetzt haben.",
            "Portuguese": "Touro valoriza estabilidade e conforto. Eles são confiáveis e persistentes quando decidem algo.",
            "Hindi": "वृषभ राशि वाले स्थिरता और आराम को महत्व देते हैं। वे भरोसेमंद होते हैं और एक बार जब वे कुछ करने का मन बना लेते हैं तो लगातार बने रहते हैं।",
            "Japanese": "牡牛座は安定と快適さを重視します。彼らは信頼でき、一度何かを決めたら粘り強いです。",
            "Russian": "Тельцы ценят стабильность и комфорт. Они надежны и настойчивы, когда решат что-то сделать.",
            "Chinese": "金牛座重视稳定和舒适。他们可靠，一旦下定决心就会坚持不懈。",
            "Arabic": "الثور يقدر الاستقرار والراحة. إنهم موثوقون ومثابرون بمجرد أن يقرروا شيئًا."
        }
    },
    "Gemini": {
        "emoji": "♊",
        "traits": {
            "English": ["Adaptable", "Outgoing", "Intelligent", "Playful", "Curious"],
            "Indonesian": ["Mudah beradaptasi", "Ramah", "Cerdas", "Lincah", "Penuh rasa ingin tahu"],
            "Spanish": ["Adaptable", "Extrovertido", "Inteligente", "Juguetón", "Curioso"],
            "French": ["Adaptable", "Sociable", "Intelligent", "Joueur", "Curieux"],
            "German": ["Anpassungsfähig", "Gesellig", "Intelligent", "Verspielt", "Neugierig"],
            "Portuguese": ["Adaptável", "Extrovertido", "Inteligente", "Brincalhão", "Curioso"],
            "Hindi": ["अनुकूलनीय", "मिलनसार", "बुद्धिमान", "चंचल", "जिज्ञासु"],
            "Japanese": ["順応性がある", "社交的", "知的", "遊び心がある", "好奇心旺盛"],
            "Russian": ["Адаптируемый", "Общительный", "Умный", "Игривый", "Любопытный"],
            "Chinese": ["适应性强", "外向", "聪明", "好玩", "好奇"],
            "Arabic": ["قابل للتكيف", "منفتح", "ذكي", "مرح", "فضولي"]
        },
        "description": {
            "English": "Geminis are quick-witted and curious. They're social butterflies who love communication.",
            "Indonesian": "Gemini cepat tanggap dan penuh rasa ingin tahu. Mereka suka bersosialisasi dan mencintai komunikasi.",
            "Spanish": "Los Géminis son ingeniosos y curiosos. Son mariposas sociales que aman la comunicación.",
            "French": "Les Gémeaux sont vifs d'esprit et curieux. Ce sont des papillons sociaux qui aiment communiquer.",
            "German": "Zwillinge sind geistesgegenwärtig und neugierig. Sie sind gesellige Menschen, die die Kommunikation lieben.",
            "Portuguese": "Gêmeos sont rápidos e curiosos. Eles são borboletas sociais que amam comunicação.",
            "Hindi": "मिथुन राशि वाले तेज दिमाग वाले और जिज्ञासु होते हैं। वे सामाजिक तितलियाँ हैं जो संचार से प्यार करते हैं।",
            "Japanese": "双子座は機知に富み、好奇心旺盛です。彼らはコミュニケーションを愛する社交的な人々です。",
            "Russian": "Близнецы сообразительны и любознательны. Они социальные бабочки, которые любят общение.",
            "Chinese": "双子座机智而好奇。他们是喜欢交流的社交蝴蝶。",
            "Arabic": "الجوزاء سريع البديهة وفضولي. هم فراشات اجتماعية تحب التواصل."
        }
    },
    "Cancer": {
        "emoji": "♋",
        "traits": {
            "English": ["Intuitive", "Emotional", "Nurturing", "Protective", "Sympathetic"],
            "Indonesian": ["Intuitif", "Emosional", "Penyayang", "Pelindung", "Simpatik"],
            "Spanish": ["Intuitivo", "Emocional", "Cariñoso", "Protector", "Compasivo"],
            "French": ["Intuitif", "Émotionnel", "Bienveillant", "Protecteur", "Compatissant"],
            "German": ["Intuitiv", "Emotional", "Fürsorglich", "Beschützend", "Mitfühlend"],
            "Portuguese": ["Intuitivo", "Emocional", "Acolhedor", "Protetor", "Compreensivo"],
            "Hindi": ["सहजज्ञ", "भावुक", "पालन-पोषण करने वाला", "सुरक्षात्मक", "हमदर्द"],
            "Japanese": ["直感的", "感情的", "世話好き", "保護的", "共感的"],
            "Russian": ["Интуитивный", "Эмоциональный", "Заботливый", "Защитный", "Сочувствующий"],
            "Chinese": ["直觉", "情绪化", "养育", "保护", "同情"],
            "Arabic": ["بديهي", "عاطفي", "رعاية", "حماية", "متعاطف"]
        },
        "description": {
            "English": "Cancers are deeply intuitive and sentimental. They value home and family above all else.",
            "Indonesian": "Cancer sangat intuitif dan sentimental. Mereka menghargai rumah dan keluarga di atas segalanya.",
            "Spanish": "Los Cáncer son profundamente intuitivos y sentimentales. Valoran el hogar y la familia por encima de todo.",
            "French": "Les Cancer sont profondément intuitifs et sentimentaux. Ils valorisent la maison et la famille par-dessus tout.",
            "German": "Krebse sind zutiefst intuitiv und sentimental. Sie schätzen Heim und Familie über alles.",
            "Portuguese": "Câncer são profundamente intuitivos e sentimentais. Eles valorizam o lar e a família acima de tudo.",
            "Hindi": "कर्क राशि वाले गहराई से सहजज्ञ और भावुक होते हैं। वे घर और परिवार को सबसे ऊपर महत्व देते हैं।",
            "Japanese": "蟹座は非常に直感的で感傷的です。彼らは何よりも家庭と家族を大切にします。",
            "Russian": "Раки глубоко интуитивны и сентиментальны. Они ценят дом и семью превыше всего.",
            "Chinese": "巨蟹座具有深刻的直觉和感伤。他们最重视家庭和家人。",
            "Arabic": "السرطان بديهي وعاطفي للغاية. إنهم يقدرون المنزل والعائلة فوق كل شيء."
        }
    },
    "Leo": {
        "emoji": "♌",
        "traits": {
            "English": ["Confident", "Generous", "Loyal", "Dramatic", "Charismatic"],
            "Indonesian": ["Percaya diri", "Dermawan", "Setia", "Dramatis", "Karismatik"],
            "Spanish": ["Seguro", "Generoso", "Leal", "Dramático", "Carismático"],
            "French": ["Confiant", "Généreux", "Loyal", "Dramatique", "Charismatique"],
            "German": ["Selbstbewusst", "Großzügig", "Loyal", "Dramatisch", "Charismatisch"],
            "Portuguese": ["Confiante", "Generoso", "Leal", "Dramático", "Carismático"],
            "Hindi": ["आत्मविश्वासी", "उदार", "वफादार", "नाटकीय", "करिश्माई"],
            "Japanese": ["自信がある", "寛大", "忠実", "ドラマチック", "カリスマ性がある"],
            "Russian": ["Уверенный", "Щедрый", "Верный", "Драматичный", "Харизматичный"],
            "Chinese": ["自信", "慷慨", "忠诚", "戏剧性", "魅力"],
            "Arabic": ["واثق", "كريم", "مخلص", "درامي", "كاريزمي"]
        },
        "description": {
            "English": "Leos are natural leaders with big hearts. They're confident and love to be in the spotlight.",
            "Indonesian": "Leo adalah pemimpin alami dengan hati yang besar. Mereka percaya diri dan suka menjadi pusat perhatian.",
            "Spanish": "Los Leo son líderes naturales con un gran corazón. Son seguros de sí mismos y les encanta ser el centro de atención.",
            "French": "Les Lions sont des leaders naturels au grand cœur. Ils sont confiants et aiment être sous les feux de la rampe.",
            "German": "Löwen sind geborene Anführer mit großem Herzen. Sie sind selbstbewusst und lieben es, im Rampenlicht zu stehen.",
            "Portuguese": "Leos são líderes naturais de coração grande. Eles são confiantes e adoram estar no centro das atenções.",
            "Hindi": "सिंह राशि वाले बड़े दिल वाले प्राकृतिक नेता होते हैं। वे आत्मविश्वासी होते हैं और स्पॉटलाइट में रहना पसंद करते हैं।",
            "Japanese": "獅子座は大きな心を持つ生まれながらのリーダーです。彼らは自信があり、注目を浴びるのが大好きです。",
            "Russian": "Львы — прирожденные лидеры с большим сердцем. Они уверены в себе и любят быть в центре внимания.",
            "Chinese": "狮子座是天生的领导者，心胸宽广。他们自信，喜欢成为焦点。",
            "Arabic": "الأسود قادة بالفطرة بقلوب كبيرة. إنهم واثقون ويحبون أن يكونوا في دائرة الضوء."
        }
    },
    "Virgo": {
        "emoji": "♍",
        "traits": {
            "English": ["Analytical", "Practical", "Precise", "Kind", "Hardworking"],
            "Indonesian": ["Analitis", "Praktis", "Tepat", "Baik hati", "Rajin"],
            "Spanish": ["Analítico", "Práctico", "Preciso", "Amable", "Trabajador"],
            "French": ["Analytique", "Pratique", "Précis", "Gentil", "Travailleur"],
            "German": ["Analytisch", "Pragmatisch", "Präzise", "Freundlich", "Fleißig"],
            "Portuguese": ["Analítico", "Prático", "Preciso", "Gentil", "Trabalhador"],
            "Hindi": ["विश्लेषणात्मक", "व्यावहारिक", "सटीक", "दयालु", "मेहनती"],
            "Japanese": ["分析的", "実用的", "正確", "親切", "勤勉"],
            "Russian": ["Аналитический", "Практичный", "Точный", "Добрый", "Трудолюбивый"],
            "Chinese": ["分析", "务实", "精确", "善良", "勤奋"],
            "Arabic": ["تحليلي", "عملي", "دقيق", "لطيف", "مجتهد"]
        },
        "description": {
            "English": "Virgos are logical and practical. They have a keen eye for detail and a strong sense of humanity.",
            "Indonesian": "Virgo logis dan praktis. Mereka memiliki mata yang tajam untuk detail dan rasa kemanusiaan yang kuat.",
            "Spanish": "Los Virgo son lógicos y prácticos. Tienen un ojo agudo para los detalles y un fuerte sentido de la humanidad.",
            "French": "Les Vierges sont logiques et pratiques. Ils ont un œil aiguisé pour les détails et un fort sens de l'humanité.",
            "German": "Jungfrauen sind logisch und praktisch veranlagt. Sie haben ein Auge für Details und einen starken Sinn für Menschlichkeit.",
            "Portuguese": "Virgens são lógicas e práticas. Eles têm um olho afiado para detalhes e um forte senso de humanidade.",
            "Hindi": "कन्या राशि वाले तार्किक और व्यावहारिक होते हैं। उनकी नजर विस्तार पर तेज होती है और मानवता की गहरी समझ होती है।",
            "Japanese": "乙女座は論理的で実用的です。彼らは細部に目が行き届き、強い人間性を持っています。",
            "Russian": "Девы логичны и практичны. Они внимательны к деталям и обладают сильным чувством человечности.",
            "Chinese": "处女座逻辑性强，务实。他们对细节有敏锐的洞察力，有强烈的人性意识。",
            "Arabic": "العذراء منطقية وعملية. لديهم عين حادة للتفاصيل وإحساس قوي بالإنسانية."
        }
    },
    "Libra": {
        "emoji": "♎",
        "traits": {
            "English": ["Diplomatic", "Social", "Fair-minded", "Gracious", "Cooperative"],
            "Indonesian": ["Diplomatis", "Sosial", "Adil", "Ramah", "Kooperatif"],
            "Spanish": ["Diplomático", "Social", "Justo", "Amable", "Cooperativo"],
            "French": ["Diplomatique", "Sociable", "Équitable", "Gracieux", "Coopératif"],
            "German": ["Diplomatisch", "Gesellig", "Fair", "Anmutig", "Kooperativ"],
            "Portuguese": ["Diplomático", "Social", "Justo", "Gracioso", "Cooperativo"],
            "Hindi": ["कूटनीतिक", "सामाजिक", "निष्पक्ष", "सुशील", "सहयोगी"],
            "Japanese": ["外交的", "社交的", "公平", "優雅", "協力的"],
            "Russian": ["Дипломатичный", "Общительный", "Справедливый", "Милостивый", "Сотрудничающий"],
            "Chinese": ["外交", "社交", "公平", "亲切", "合作"],
            "Arabic": ["دبلوماسي", "اجتماعي", "عادل", "رقيق", "متعاون"]
        },
        "description": {
            "English": "Libras value harmony and balance. They're natural peacemakers with a strong sense of justice.",
            "Indonesian": "Libra menghargai harmoni dan keseimbangan. Mereka adalah pembawa perdamaian alami dengan rasa keadilan yang kuat.",
            "Spanish": "Los Libra valoran la armonía y el equilibrio. Son pacificadores naturales con un fuerte sentido de la justicia.",
            "French": "Les Balance valorisent l'harmonie et l'équilibre. Ce sont des pacificateurs naturels avec un fort sens de la justice.",
            "German": "Waagen schätzen Harmonie und Gleichgewicht. Sie sind geborene Friedensstifter mit einem starken Gerechtigkeitssinn.",
            "Portuguese": "Librianos valorizam harmonia e equilíbrio. Eles são pacificadores naturais com um forte senso de justiça.",
            "Hindi": "तुला राशि वाले सद्भाव और संतुलन को महत्व देते हैं। वे न्याय की मजबूत भावना वाले प्राकृतिक शांतिदूत हैं।",
            "Japanese": "天秤座は調和とバランスを重視します。彼らは正義感の強い生まれながらの平和主義者です。",
            "Russian": "Весы ценят гармонию и баланс. Они прирожденные миротворцы с обостренным чувством справедливости.",
            "Chinese": "天秤座重视和谐与平衡。他们是具有强烈正义感的天生和事佬。",
            "Arabic": "الميزان يقدرون الانسجام والتوازن. إنهم صانعو سلام بالفطرة يتمتعون بإحساس قوي بالعدالة."
        }
    },
    "Scorpio": {
        "emoji": "♏",
        "traits": {
            "English": ["Passionate", "Determined", "Intense", "Loyal", "Brave"],
            "Indonesian": ["Bersemangat", "Bertekad", "Intens", "Setia", "Berani"],
            "Spanish": ["Apasionado", "Determinado", "Intenso", "Leal", "Valiente"],
            "French": ["Passionné", "Déterminé", "Intense", "Loyal", "Courageux"],
            "German": ["Leidenschaftlich", "Entschlossen", "Intensiv", "Loyal", "Mutig"],
            "Portuguese": ["Apaixonado", "Determinado", "Intenso", "Leal", "Corajoso"],
            "Hindi": ["जुनूनी", "दृढ़ निश्चयी", "तीव्र", "वफादार", "बहादुर"],
            "Japanese": ["情熱的", "決断力がある", "激しい", "忠実", "勇敢"],
            "Russian": ["Страстный", "Решительный", "Интенсивный", "Верный", "Храбрый"],
            "Chinese": ["热情", "坚决", "激烈", "忠诚", "勇敢"],
            "Arabic": ["شغوف", "مصمم", "مكثف", "مخلص", "شجاع"]
        },
        "description": {
            "English": "Scorpios are passionate and assertive. They're resourceful and brave with strong intuition.",
            "Indonesian": "Scorpio penuh gairah dan tegas. Mereka pandai dan berani dengan intuisi yang kuat.",
            "Spanish": "Los Escorpio son apasionados y asertivos. Son ingeniosos y valientes con una intuición fuerte.",
            "French": "Les Scorpion sont passionnés et affirmés. Ils sont débrouillards et courageux avec une forte intuition.",
            "German": "Skorpione sind leidenschaftlich et durchsetzungsfähig. Sie sind einfallsreich und mutig mit einer starken Intuition.",
            "Portuguese": "Escorpiões são apaixonados e assertivos. Eles são engenhosos e corajosos com forte intuição.",
            "Hindi": "वृश्चिक राशि वाले जुनूनी और मुखर होते हैं। वे मजबूत अंतर्ज्ञान के साथ साहसी और बहादुर होते हैं।",
            "Japanese": "蠍座は情熱的で自己主張が強いです。彼らは強い直感を持ち、機知に富み、勇敢です。",
            "Russian": "Скорпионы страстны и напористы. Они находчивы и храбры с сильной интуицией.",
            "Chinese": "天蝎座热情而自信。他们足智多谋，勇敢，直觉敏锐。",
            "Arabic": "العقارب شغوفون وحازمون. إنهم ماهرون وشجعان مع حدس قوي."
        }
    },
    "Sagittarius": {
        "emoji": "♐",
        "traits": {
            "English": ["Adventurous", "Optimistic", "Honest", "Philosophical", "Generous"],
            "Indonesian": ["Petualang", "Optimis", "Jujur", "Filosofis", "Dermawan"],
            "Spanish": ["Aventurero", "Optimista", "Honesto", "Filosófico", "Generoso"],
            "French": ["Aventureux", "Optimiste", "Honnête", "Philosophique", "Généreux"],
            "German": ["Abenteuerlustig", "Optimistisch", "Ehrlich", "Philosophisch", "Großzügig"],
            "Portuguese": ["Aventureiro", "Otimista", "Honesto", "Filosófico", "Generoso"],
            "Hindi": ["साहसी", "आशावादी", "ईमानदार", "दार्शनिक", "उदार"],
            "Japanese": ["冒険好き", "楽観的", "正直", "哲学的", "寛大"],
            "Russian": ["Приключенческий", "Оптимистичный", "Честный", "Философский", "Щедрый"],
            "Chinese": ["冒险", "乐观", "诚实", "哲学", "慷慨"],
            "Arabic": ["مغامر", "متفائل", "صادق", "فلسفي", "كريم"]
        },
        "description": {
            "English": "Sagittarians are free-spirited and love adventure. They're optimistic and always looking for meaning.",
            "Indonesian": "Sagitarius berjiwa bebas dan mencintai petualangan. Mereka optimis dan selalu mencari makna.",
            "Spanish": "Los Sagitario son de espíritu libre y aman la aventura. Son optimistas y siempre buscan significado.",
            "French": "Les Sagittaire sont libres d'esprit et aiment l'aventure. Ils sont optimistes et toujours à la recherche de sens.",
            "German": "Schützen sind freiheitsliebend und lieben Abenteuer. Sie sind optimistisch und immer auf der Suche nach Bedeutung.",
            "Portuguese": "Sagitarianos são livres e amam aventuras. Eles sont otimistas e sempre procuram significado.",
            "Hindi": "धनु राशि वाले स्वतंत्र विचारों वाले होते हैं और साहसिक कार्यों से प्यार करते हैं। वे आशावादी होते हैं और हमेशा अर्थ की तलाश में रहते हैं।",
            "Japanese": "射手座は自由奔放で冒険が大好きです。彼らは楽観的で、常に意味を探しています。",
            "Russian": "Стрельцы свободолюбивы и любят приключения. Они оптимистичны и всегда ищут смысл.",
            "Chinese": "射手座自由奔放，热爱冒险。他们乐观，总是在寻找意义。",
            "Arabic": "القوس أحرار الروح ويحبون المغامرة. إنهم متفائلون ويبحثون دائمًا عن المعنى."
        }
    }
}

# Language translations
translations = {
    "English": {
        "title": "Zodiac Finder & Personality Traits",
        "description": "Discover your astrological sign and personality traits based on your birth date.",
        "name_prompt": "Enter your name:",
        "month_prompt": "Select your birth month:",
        "day_prompt": "Enter your birth day (1-31):",
        "year_prompt": "Enter year (for February 29 validation):",
        "button_text": "Find My Zodiac Sign",
        "valid_date": "Valid date: {}, {}",
        "result": "Hello, **{}**! Your zodiac sign is: **{} {}**",
        "invalid_date": "❌ Invalid date! That day doesn't exist in that month.",
        "fun_fact": "Fun Fact",
        "fun_fact_water": "As a Water sign, you're likely deeply intuitive and emotional!",
        "fun_fact_fire": "As a Fire sign, you're probably passionate and dynamic!",
        "fun_fact_air": "As an Air sign, you're likely intellectual and communicative!",
        "fun_fact_earth": "As an Earth sign, you're probably practical and grounded!",
        "compatible": "Most compatible with:",
        "incompatible": "Challenging matches:",
        "traits_title": "Personality Traits {}",
        "key_traits": "Key Traits:"
    },
    "Indonesian": {
        "title": "Zodiac Finder & Personality Traits",
        "description": "Temukan tanda zodiak dan sifat kepribadian Anda berdasarkan tanggal lahir.",
        "name_prompt": "Masukkan nama Anda:",
        "month_prompt": "Pilih bulan kelahiran Anda:",
        "day_prompt": "Masukkan tanggal lahir (1-31):",
        "year_prompt": "Masukkan tahun (untuk validasi 29 Februari):",
        "button_text": "Cari Zodiak Saya",
        "valid_date": "Tanggal valid: {}, {}",
        "result": "Halo, **{}**! Zodiak Anda adalah: **{} {}**",
        "invalid_date": "❌ Tanggal tidak valid! Tanggal tersebut tidak ada di bulan itu.",
        "fun_fact": "Fakta Menarik",
        "fun_fact_water": "Sebagai tanda Air, Anda mungkin sangat intuitif dan emosional!",
        "fun_fact_fire": "Sebagai tanda Api, Anda mungkin penuh gairah dan dinamis!",
        "fun_fact_air": "Sebagai tanda Udara, Anda mungkin intelektual dan komunikatif!",
        "fun_fact_earth": "Sebagai tanda Tanah, Anda mungkin praktis dan berpijak pada realita!",
        "compatible": "Paling cocok dengan:",
        "incompatible": "Kesulitan dengan:",
        "traits_title": "Sifat Kepribadian {}",
        "key_traits": "Sifat Utama:"
    },
    "Spanish": {
        "title": "Zodiac Finder & Personality Traits",
        "description": "Descubre tu signo astrológico y rasgos de personalidad según tu fecha de nacimiento.",
        "name_prompt": "Ingresa tu nombre:",
        "month_prompt": "Selecciona tu mes de nacimiento:",
        "day_prompt": "Ingresa tu día de nacimiento (1-31):",
        "year_prompt": "Ingresa año (para validación 29 de febrero):",
        "button_text": "Encontrar Mi Signo Zodiacal",
        "valid_date": "Fecha válida: {}, {}",
        "result": "¡Hola, **{}**! Tu signo zodiacal es: **{} {}**",
        "invalid_date": "❌ ¡Fecha inválida! Ese día no existe en ese mes.",
        "fun_fact": "Dato Curioso",
        "fun_fact_water": "¡Como signo de Agua, es probable que seas muy intuitivo y emocional!",
        "fun_fact_fire": "¡Como signo de Fuego, probablemente eres apasionado y dinámico!",
        "fun_fact_air": "¡Como signo de Aire, es probable que seas intelectual y comunicativo!",
        "fun_fact_earth": "¡Como signo de Tierra, probablemente eres práctico y con los pies en la tierra!",
        "compatible": "Más compatible con:",
        "incompatible": "Desafíos con:",
        "traits_title": "Rasgos de Personalidad {}",
        "key_traits": "Rasgos Clave:"
    },
    "French": {
        "title": "Zodiac Finder & Personality Traits",
        "description": "Découvrez votre signe astrologique et vos traits de personnalité basés sur votre date de naissance.",
        "name_prompt": "Entrez votre nom:",
        "month_prompt": "Sélectionnez votre mois de naissance:",
        "day_prompt": "Entrez votre jour de naissance (1-31):",
        "year_prompt": "Entrez l'année (pour validation 29 février):",
        "button_text": "Trouver Mon Signe Zodiacal",
        "valid_date": "Date valide: {}, {}",
        "result": "Bonjour, **{}**! Votre signe zodiacal est: **{} {}**",
        "invalid_date": "❌ Date invalide! Ce jour n'existe pas dans ce mois.",
        "fun_fact": "Fait Amusant",
        "fun_fact_water": "En tant que signe d'Eau, vous êtes probablement très intuitif et émotionnel!",
        "fun_fact_fire": "En tant que signe de Feu, vous êtes probablement passionné et dynamique!",
        "fun_fact_air": "En tant que signe d'Air, vous êtes probablement intellectuel et communicatif!",
        "fun_fact_earth": "En tant que signe de Terre, vous êtes probablement pratique et terre-à-terre!",
        "compatible": "Plus compatible avec:",
        "incompatible": "Défis avec:",
        "traits_title": "Traits de Personnalité {}",
        "key_traits": "Traits Clés:"
    },
    "German": {
        "title": "Zodiac Finder & Personality Traits",
        "description": "Entdecken Sie Ihr Sternzeichen und Persönlichkeitsmerkmale basierend auf Ihrem Geburtsdatum.",
        "name_prompt": "Geben Sie Ihren Namen ein:",
        "month_prompt": "Wählen Sie Ihren Geburtsmonat:",
        "day_prompt": "Geben Sie Ihren Geburtstag ein (1-31):",
        "year_prompt": "Geben Sie das Jahr ein (für 29. Februar Validierung):",
        "button_text": "Mein Sternzeichen Finden",
        "valid_date": "Gültiges Datum: {}, {}",
        "result": "Hallo, **{}**! Ihr Sternzeichen ist: **{} {}**",
        "invalid_date": "❌ Ungültiges Datum! Dieser Tag existiert in diesem Monat nicht.",
        "fun_fact": "Interessante Tatsache",
        "fun_fact_water": "Als Wasserzeichen sind Sie wahrscheinlich sehr intuitiv und emotional!",
        "fun_fact_fire": "Als Feuerzeichen sind Sie wahrscheinlich leidenschaftlich und dynamisch!",
        "fun_fact_air": "Als Luftzeichen sind Sie wahrscheinlich intellektuell und kommunikativ!",
        "fun_fact_earth": "Als Erdzeichen sind Sie wahrscheinlich praktisch und bodenständig!",
        "compatible": "Am besten verträglich mit:",
        "incompatible": "Herausforderungen mit:",
        "traits_title": "Persönlichkeitsmerkmale {}",
        "key_traits": "Hauptmerkmale:"
    },
    "Portuguese": {
        "title": "Zodiac Finder & Personality Traits",
        "description": "Descubra seu signo astrológico e traços de personalidade com base em sua data de nascimento.",
        "name_prompt": "Digite seu nome:",
        "month_prompt": "Selecione seu mês de nascimento:",
        "day_prompt": "Digite seu dia de nascimento (1-31):",
        "year_prompt": "Digite o ano (para validação 29 de fevereiro):",
        "button_text": "Encontrar Meu Signo",
        "valid_date": "Data válida: {}, {}",
        "result": "Olá, **{}**! Seu signo zodiacal é: **{} {}**",
        "invalid_date": "❌ Data inválida! Esse dia não existe nesse mês.",
        "fun_fact": "Curiosidade",
        "fun_fact_water": "Como signo de Água, você provavelmente é muito intuitivo e emocional!",
        "fun_fact_fire": "Como signo de Fogo, você provavelmente é apaixonado e dinâmico!",
        "fun_fact_air": "Como signo de Ar, você provavelmente é intelectual e comunicativo!",
        "fun_fact_earth": "Como signo de Terra, você provavelmente é prático e com os pés no chão!",
        "compatible": "Mais compatível com:",
        "incompatible": "Desafios com:",
        "traits_title": "Traços de Personalidade {}",
        "key_traits": "Traços Principais:"
    },
    "Hindi": {
        "title": "Zodiac Finder & Personality Traits",
        "description": "अपनी जन्म तिथि के आधार पर अपना राशि चिन्ह और व्यक्तित्व लक्षण खोजें।",
        "name_prompt": "अपना नाम दर्ज करें:",
        "month_prompt": "अपना जन्म माह चुनें:",
        "day_prompt": "अपना जन्म दिन दर्ज करें (1-31):",
        "year_prompt": "वर्ष दर्ज करें (29 फरवरी सत्यापन के लिए):",
        "button_text": "मेरी राशि खोजें",
        "valid_date": "मान्य तिथि: {}, {}",
        "result": "नमस्ते, **{}**! आपकी राशि है: **{} {}**",
        "invalid_date": "❌ अमान्य तिथि! उस महीने में वह दिन मौजूद नहीं है।",
        "fun_fact": "रोचक तथ्य",
        "fun_fact_water": "जल राशि के रूप में, आप संभवतः गहराई से सहज और भावुक हैं!",
        "fun_fact_fire": "अग्नि राशि के रूप में, आप संभवतः जोशीले और गतिशील हैं!",
        "fun_fact_air": "वायु राशि के रूप में, आप संभवतः बौद्धिक और संचार कुशल हैं!",
        "fun_fact_earth": "पृथ्वी राशि के रूप में, आप संभवतः व्यावहारिक और जमीन से जुड़े हैं!",
        "compatible": "सबसे अधिक संगत:",
        "incompatible": "चुनौतियाँ:",
        "traits_title": "व्यक्तित्व लक्षण {}",
        "key_traits": "मुख्य लक्षण:"
    },
    "Japanese": {
        "title": "Zodiac Finder & Personality Traits",
        "description": "生年月日に基づいてあなたの星座と性格特性を発見してください。",
        "name_prompt": "名前を入力してください:",
        "month_prompt": "生まれた月を選択してください:",
        "day_prompt": "誕生日を入力してください (1-31):",
        "year_prompt": "年を入力してください (2月29日検証用):",
        "button_text": "私の星座を見つける",
        "valid_date": "有効な日付: {}, {}",
        "result": "こんにちは、**{}**さん！ あなたの星座は **{} {}** です",
        "invalid_date": "❌ 無効な日付！ その月にその日は存在しません。",
        "fun_fact": "豆知識",
        "fun_fact_water": "水の星座として、あなたはおそらく非常に直感的で感情的です！",
        "fun_fact_fire": "火の星座として、あなたはおそらく情熱的でダイナミックです！",
        "fun_fact_air": "風の星座として、あなたはおそらく知的でコミュニケーション能力が高いです！",
        "fun_fact_earth": "地の星座として、あなたはおそらく実用的で現実的です！",
        "compatible": "最も相性が良い:",
        "incompatible": "相性の課題:",
        "traits_title": "性格特性 {}",
        "key_traits": "主な特性:"
    },
    "Russian": {
        "title": "Zodiac Finder & Personality Traits",
        "description": "Узнайте свой астрологический знак и черты личности на основе даты рождения.",
        "name_prompt": "Введите ваше имя:",
        "month_prompt": "Выберите месяц рождения:",
        "day_prompt": "Введите день рождения (1-31):",
        "year_prompt": "Введите год (для проверки 29 февраля):",
        "button_text": "Найти Мой Знак Зодиака",
        "valid_date": "Действительная дата: {}, {}",
        "result": "Привет, **{}**! Ваш знак зодиака: **{} {}**",
        "invalid_date": "❌ Неверная дата! Этого дня нет в указанном месяце.",
        "fun_fact": "Интересный факт",
        "fun_fact_water": "Как водный знак, вы, вероятно, очень интуитивны и эмоциональны!",
        "fun_fact_fire": "Как огненный знак, вы, вероятно, страстны и динамичны!",
        "fun_fact_air": "Как воздушный знак, вы, вероятно, интеллектуальны и коммуникабельны!",
        "fun_fact_earth": "Как земной знак, вы, вероятно, практичны и приземлены!",
        "compatible": "Наиболее совместимы с:",
        "incompatible": "Сложности с:",
        "traits_title": "Черты личности {}",
        "key_traits": "Ключевые черты:"
    },
    "Chinese": {
        "title": "Zodiac Finder & Personality Traits",
        "description": "根据您的出生日期发现您的星座和个性特征。",
        "name_prompt": "输入您的名字:",
        "month_prompt": "选择您的出生月份:",
        "day_prompt": "输入您的出生日 (1-31):",
        "year_prompt": "输入年份 (用于2月29日验证):",
        "button_text": "查找我的星座",
        "valid_date": "有效日期: {}, {}",
        "result": "你好，**{}**！ 你的星座是: **{} {}**",
        "invalid_date": "❌ 无效日期！ 该月份中没有这一天。",
        "fun_fact": "有趣的事实",
        "fun_fact_water": "作为水象星座，您可能非常直觉和情绪化！",
        "fun_fact_fire": "作为火象星座，您可能充满激情和活力！",
        "fun_fact_air": "作为风象星座，您可能聪明且善于沟通！",
        "fun_fact_earth": "作为土象星座，您可能务实且脚踏实地！",
        "compatible": "最兼容:",
        "incompatible": "挑战匹配:",
        "traits_title": "个性特征 {}",
        "key_traits": "关键特征:"
    },
    "Arabic": {
        "title": "Zodiac Finder & Personality Traits",
        "description": "اكتشف علامتك الفلكية وسمات الشخصية بناءً على تاريخ ميلادك.",
        "name_prompt": "أدخل اسمك:",
        "month_prompt": "حدد شهر ميلادك:",
        "day_prompt": "أدخل يوم ميلادك (1-31):",
        "year_prompt": "أدخل السنة (للتحقق من 29 فبراير):",
        "button_text": "ابحث عن علامتي الفلكية",
        "valid_date": "تاريخ صالح: {}, {}",
        "result": "مرحبًا **{}**! علامتك الفلكية هي: **{} {}**",
        "invalid_date": "❌ تاريخ غير صالح! هذا اليوم غير موجود في هذا الشهر.",
        "fun_fact": "حقيقة ممتعة",
        "fun_fact_water": "بصفتك من علامة الماء، من المحتمل أن تكون بديهيًا وعاطفيًا!",
        "fun_fact_fire": "بصفتك من علامة النار، من المحتمل أن تكون شغوفًا وديناميكيًا!",
        "fun_fact_air": "بصفتك من علامة الهواء، من المحتمل أن تكون فكريًا وتواصليًا!",
        "fun_fact_earth": "بصفتك من علامة الأرض، من المحتمل أن تكون عمليًا وواقعيًا!",
        "compatible": "الأكثر توافقًا مع:",
        "incompatible": "تحديات مع:",
        "traits_title": "سمات الشخصية {}",
        "key_traits": "السمات الرئيسية:"
    }
}


def show_progress(duration=3, width=20):
    progress_bar = st.progress(0)
    for i in range(width + 1):
        percent = int((i / width) * 100)
        progress_bar.progress(percent)
        time.sleep(duration / width)


def get_zodiac(month, day):
    month = month.lower()
    if (month == "december" and day >= 22) or (month == "january" and day <= 19):
        return "Capricorn"
    elif (month == "january" and day >= 20) or (month == "february" and day <= 18):
        return "Aquarius"
    elif (month == "february" and day >= 19) or (month == "march" and day <= 20):
        return "Pisces"
    elif (month == "march" and day >= 21) or (month == "april" and day <= 19):
        return "Aries"
    elif (month == "april" and day >= 20) or (month == "may" and day <= 20):
        return "Taurus"
    elif (month == "may" and day >= 21) or (month == "june" and day <= 20):
        return "Gemini"
    elif (month == "june" and day >= 21) or (month == "july" and day <= 22):
        return "Cancer"
    elif (month == "july" and day >= 23) or (month == "august" and day <= 22):
        return "Leo"
    elif (month == "august" and day >= 23) or (month == "september" and day <= 22):
        return "Virgo"
    elif (month == "september" and day >= 23) or (month == "october" and day <= 22):
        return "Libra"
    elif (month == "october" and day >= 23) or (month == "november" and day <= 21):
        return "Scorpio"
    elif (month == "november" and day >= 22) or (month == "december" and day <= 21):
        return "Sagittarius"
    return "Unknown"


def is_valid_date(month, day, year=None):
    month = month.lower()
    max_days = {
        "january": 31, "february": 29 if year and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 28,
        "march": 31, "april": 30, "may": 31, "june": 30,
        "july": 31, "august": 31, "september": 30,
        "october": 31, "november": 30, "december": 31
    }

    if month not in max_days:
        return False

    return 1 <= day <= max_days[month]


def display_personality_traits(zodiac_sign, language):
    if zodiac_sign not in zodiac_data:
        st.error("Invalid zodiac sign!")
        return

    data = zodiac_data[zodiac_sign]
    lang = translations[language]

    st.subheader(lang["traits_title"].format(data['emoji']))
    st.write(data['description'][language])

    st.write(f"**{lang['key_traits']}**")
    cols = st.columns(3)
    for i, trait in enumerate(data['traits'][language]):
        cols[i % 3].success(f"✓ {trait}")

    st.subheader(lang["compatible"])
    compatible = []
    incompatible = []

    # Simple compatibility logic
    if zodiac_sign in ["Aries", "Leo", "Sagittarius"]:  # Fire signs
        compatible.extend(["Leo", "Sagittarius", "Gemini", "Libra"])
        incompatible.extend(["Cancer", "Capricorn", "Virgo"])
    elif zodiac_sign in ["Taurus", "Virgo", "Capricorn"]:  # Earth signs
        compatible.extend(["Virgo", "Capricorn", "Cancer", "Pisces"])
        incompatible.extend(["Aries", "Libra", "Aquarius"])
    elif zodiac_sign in ["Gemini", "Libra", "Aquarius"]:  # Air signs
        compatible.extend(["Libra", "Aquarius", "Aries", "Sagittarius"])
        incompatible.extend(["Taurus", "Scorpio", "Pisces"])
    else:  # Water signs
        compatible.extend(["Scorpio", "Pisces", "Taurus", "Cancer"])
        incompatible.extend(["Gemini", "Sagittarius", "Leo"])

    st.write(f"**{lang['compatible']}** " + ", ".join(list(set(compatible))))
    st.write(f"**{lang['incompatible']}** " + ", ".join(list(set(incompatible))))

    # Fun fact section
    st.subheader(lang["fun_fact"])
    if zodiac_sign in ["Cancer", "Scorpio", "Pisces"]:
        st.info(lang["fun_fact_water"])
    elif zodiac_sign in ["Aries", "Leo", "Sagittarius"]:
        st.info(lang["fun_fact_fire"])
    elif zodiac_sign in ["Gemini", "Libra", "Aquarius"]:
        st.info(lang["fun_fact_air"])
    else:
        st.info(lang["fun_fact_earth"])


# Streamlit UI
def main():
    st.set_page_config(page_title="Zodiac Finder", page_icon="♈", layout="centered")

    # Language selection dropdown
    selected_language = st.sidebar.selectbox(
        "Select Language",
        list(translations.keys()),
        index=0  # Default to English
    )

    lang = translations[selected_language]

    st.title(lang["title"])
    st.markdown(lang["description"])

    # Get user input
    name = st.text_input(lang["name_prompt"])

    if name:  # Only proceed if name is entered
        birth_month = st.selectbox(
            lang["month_prompt"],
            ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
        )

        birth_day = st.number_input(lang["day_prompt"], min_value=1, max_value=31)

        # Only ask for year if February is selected
        year = None
        if birth_month.lower() == "february" and birth_day == 29:
            year = st.number_input(
                lang["year_prompt"],
                min_value=1900,
                max_value=2100,
                value=2000
            )

        if st.button(lang["button_text"]):
            if is_valid_date(birth_month, birth_day, year):
                st.success(lang["valid_date"].format(birth_month, birth_day))
                show_progress()
                zodiac_sign = get_zodiac(birth_month, birth_day)

                # Main result
                data = zodiac_data[zodiac_sign]
                st.success(lang["result"].format(name, zodiac_sign, data['emoji']))

                # Display personality section
                display_personality_traits(zodiac_sign, selected_language)

            else:
                st.error(lang["invalid_date"])


if __name__ == "__main__":
    main()
