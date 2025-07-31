"""
获取声音模型
"""
import httpx
from sanic import Request
from lib.app_core import app
from lib.app_core.global_context import global_context

builtin_voice_models = [
    {
        "voice_id": "English_expressive_narrator",
        "description": "An expressive adult male voice with a British accent, perfect for engaging audiobook narration.",
        "voice_name": "Expressive Narrator",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_radiant_girl",
        "description": "A radiant and lively young adult female voice with a general American accent, full of energy and brightness.",
        "voice_name": "Radiant Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_magnetic_voiced_man",
        "description": "A magnetic and persuasive adult male voice with a general American accent, ideal for advertisements and promotions.",
        "voice_name": "Magnetic-voiced Male",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_compelling_lady1",
        "description": "A compelling adult female voice with a British accent, suitable for broadcast and formal announcements. Clear and authoritative.",
        "voice_name": "Compelling Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Aussie_Bloke",
        "description": "A friendly, bright adult male voice with a distinct Australian accent, conveying a cheerful and approachable tone.",
        "voice_name": "Aussie Bloke",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_captivating_female1",
        "description": "A captivating adult female voice with a general American accent, ideal for news reporting and documentary narration.",
        "voice_name": "Captivating Female",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Upbeat_Woman",
        "description": "An upbeat and bright adult female voice with a general American accent, perfect for energetic and positive messaging.",
        "voice_name": "Upbeat Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Trustworth_Man",
        "description": "A trustworthy and resonant adult male voice with a general American accent, conveying sincerity and reliability.",
        "voice_name": "Trustworthy Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_CalmWoman",
        "description": "A calm and soothing adult female voice with a general American accent, excellent for audiobooks and meditation guides.",
        "voice_name": "Calm Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_UpsetGirl",
        "description": "A young adult female voice with a British accent, effectively conveying sadness and distress.",
        "voice_name": "Upset Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Gentle-voiced_man",
        "description": "A gentle and resonant adult male voice with a general American accent, warm and reassuring.",
        "voice_name": "Gentle-voiced Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Whispering_girl",
        "description": [],
        "voice_name": "Whispering girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Diligent_Man",
        "description": "A diligent and sincere adult male voice with an Indian accent, conveying honesty and hard work.",
        "voice_name": "Diligent Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Graceful_Lady",
        "description": "A graceful and elegant middle-aged female voice with a classic British accent, exuding sophistication.",
        "voice_name": "Graceful Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_ReservedYoungMan",
        "description": "A reserved and cold adult male voice with a general American accent, conveying distance and introspection.",
        "voice_name": "Reserved Young Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_PlayfulGirl",
        "description": "A playful female youth voice with a general American accent, ideal for cartoons and children's entertainment.",
        "voice_name": "Playful Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_ManWithDeepVoice",
        "description": "An adult male with a deep, commanding voice and a general American accent, projecting authority and strength.",
        "voice_name": "Man With Deep Voice",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_MaturePartner",
        "description": "A mature, gentle middle-aged male voice with a British accent, suitable for a caring and supportive partner role.",
        "voice_name": "Mature Partner",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_FriendlyPerson",
        "description": "A friendly and natural-sounding adult male voice with a general American accent, like an approachable guy-next-door.",
        "voice_name": "Friendly Guy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_MatureBoss",
        "description": "A mature, middle-aged female voice with a general American accent, conveying authority and a commanding presence.",
        "voice_name": "Bossy Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Debator",
        "description": "A tough, middle-aged male voice with a general American accent, perfect for debates and assertive arguments.",
        "voice_name": "Male Debater",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_LovelyGirl",
        "description": "A lovely and sweet female youth voice with a British accent, full of charm and innocence.",
        "voice_name": "Lovely Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Steadymentor",
        "description": "A young adult male voice with a general American accent, projecting an air of arrogant reliability.",
        "voice_name": "Reliable Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Deep-VoicedGentleman",
        "description": "A deep-voiced and wise adult male gentleman with a classic British accent, sounding experienced and thoughtful.",
        "voice_name": "Deep-voiced Gentleman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Wiselady",
        "description": "A wise and genial middle-aged female voice with a British accent, offering kind and insightful words.",
        "voice_name": "Wise Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_CaptivatingStoryteller",
        "description": "A captivating senior male storyteller with a cold, detached tone and a general American accent.",
        "voice_name": "Captivating Storyteller",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_DecentYoungMan",
        "description": "A decent and respectable adult male voice with a British accent, sounding polite and well-mannered.",
        "voice_name": "Decent Young Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_SentimentalLady",
        "description": "A sentimental and elegant middle-aged female voice with a British accent, perfect for nostalgic or emotional readings.",
        "voice_name": "Sentimental Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_ImposingManner",
        "description": "The imposing voice of an adult queen with a powerful British accent, commanding respect and authority.",
        "voice_name": "Imposing Queen",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_SadTeen",
        "description": "A frustrated young adult male voice with a British accent, perfect for a teen character expressing annoyance.",
        "voice_name": "Teen Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_PassionateWarrior",
        "description": "An energetic and passionate young adult male warrior voice with a general American accent, ready for battle.",
        "voice_name": "Passionate Warrior",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_WiseScholar",
        "description": "A wise, conversational young adult scholar with a British accent, making complex topics accessible and engaging.",
        "voice_name": "Wise Scholar",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Soft-spokenGirl",
        "description": "An adorable, soft-spoken female youth voice with a general American accent, gentle and sweet.",
        "voice_name": "Soft-Spoken Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_SereneWoman",
        "description": "A serene and friendly young adult female voice with a general American accent, calm and welcoming.",
        "voice_name": "Serene Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_ConfidentWoman",
        "description": "A confident and firm young adult female voice with a general American accent, assertive and clear.",
        "voice_name": "Confident Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_PatientMan",
        "description": "A patient adult male voice with a British accent, speaking in a calm and understanding manner.",
        "voice_name": "Patient Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Comedian",
        "description": "A breezy young adult male comedian with a British accent, delivering lines with a light and humorous touch.",
        "voice_name": "Comedian",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_BossyLeader",
        "description": "A bossy adult male leader with a general American accent, speaking unconcernedly with an air of command.",
        "voice_name": "Bossy Leader",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Strong-WilledBoy",
        "description": "A mature-sounding and strong-willed young adult male with a British accent, showing determination beyond his years.",
        "voice_name": "Strong-Willed Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_StressedLady",
        "description": "An unsure, stressed middle-aged female voice with a general American accent, conveying anxiety and uncertainty.",
        "voice_name": "Stressed Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_AssertiveQueen",
        "description": "An assertive yet guarded young adult queen with a general American accent, projecting authority while remaining cautious.",
        "voice_name": "Assertive Queen",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_AnimeCharacter",
        "description": "A sincere middle-aged female narrator with a British accent, perfect for trustworthy and heartfelt storytelling.",
        "voice_name": "Female Narrator",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Jovialman",
        "description": "A jovial and mature middle-aged male voice with a general American accent, cheerful and good-natured.",
        "voice_name": "Jovial Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_WhimsicalGirl",
        "description": "A whimsical yet wary young adult female voice with a general American accent, combining playfulness with caution.",
        "voice_name": "Whimsical Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "English_Kind-heartedGirl",
        "description": "A kind-hearted and calm young adult female with a general American accent, speaking with gentle warmth.",
        "voice_name": "Kind-Hearted Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Reliable_Executive",
        "description": "A steady and reliable middle-aged male executive voice in Standard Mandarin, conveying trustworthiness.",
        "voice_name": "Reliable Executive",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_News_Anchor",
        "description": "A professional, broadcaster-like middle-aged female news anchor in Standard Mandarin.",
        "voice_name": "News Anchor",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Unrestrained_Young_Man",
        "description": "An unrestrained and free-spirited adult male voice in Standard Mandarin.",
        "voice_name": "Unrestrained Young Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Mature_Woman",
        "description": "A charming and mature adult female voice in Standard Mandarin.",
        "voice_name": "Mature Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Arrogant_Miss",
        "description": "An arrogant adult female voice in Standard Mandarin, projecting confidence and superiority.",
        "voice_name": "Arrogant Miss",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Robot_Armor",
        "description": "An electronic, robotic adult male voice, suitable for sci-fi or futuristic content in Standard Mandarin.",
        "voice_name": "Robot Armor",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Kind-hearted_Antie",
        "description": "A gentle and kind-hearted middle-aged \"antie\" voice in Standard Mandarin, warm and caring.",
        "voice_name": "Kind-hearted Antie",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_HK_Flight_Attendant",
        "description": "A polite middle-aged female flight attendant with a Southern Chinese accent, clear and courteous.",
        "voice_name": "HK Flight Attendant",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Humorous_Elder",
        "description": "A refreshing and humorous senior male voice with a Northern Chinese accent, full of character.",
        "voice_name": "Humorous Elder",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Gentleman",
        "description": "A magnetic and charismatic adult male gentleman in Standard Mandarin.",
        "voice_name": "Gentleman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Warm_Bestie",
        "description": "A warm and crisp adult female \"bestie\" voice in Standard Mandarin, friendly and clear.",
        "voice_name": "Warm Bestie",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Stubborn_Friend",
        "description": "An uninhibited and stubborn adult male friend's voice in Standard Mandarin.",
        "voice_name": "Stubborn Friend",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Sweet_Lady",
        "description": "A tender and sweet adult female voice in Standard Mandarin.",
        "voice_name": "Sweet Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Southern_Young_Man",
        "description": "An earnest adult male voice with a Southern Chinese accent.",
        "voice_name": "Southern Young Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Wise_Women",
        "description": "A lyrical and wise middle-aged female voice in Standard Mandarin.",
        "voice_name": "Wise Women",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Gentle_Youth",
        "description": "A gentle adult male youth voice in Standard Mandarin.",
        "voice_name": "Gentle Youth",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Warm_Girl",
        "description": "A soft and warm young adult female voice in Standard Mandarin.",
        "voice_name": "Warm Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Male_Announcer",
        "description": "A magnetic middle-aged male announcer voice in Standard Mandarin, clear and authoritative.",
        "voice_name": "Male Announcer",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Kind-hearted_Elder",
        "description": "A kind and gentle senior female voice in Standard Mandarin.",
        "voice_name": "Kind-hearted Elder",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Cute_Spirit",
        "description": "An adorable and cute female spirit voice, youthful and sweet, in Standard Mandarin.",
        "voice_name": "Cute Spirit",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Radio_Host",
        "description": "A poetic adult male radio host in Standard Mandarin, with a smooth and engaging delivery.",
        "voice_name": "Radio Host",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Lyrical_Voice",
        "description": "A mellow and lyrical adult male voice in Standard Mandarin, smooth and expressive.",
        "voice_name": "Lyrical Voice",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Straightforward_Boy",
        "description": "A thoughtful and straightforward young adult male voice in Standard Mandarin.",
        "voice_name": "Straightforward Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Sincere_Adult",
        "description": "A sincere and encouraging adult male voice in Standard Mandarin.",
        "voice_name": "Sincere Adult",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Gentle_Senior",
        "description": "A gentle and cozy adult female senior voice in Standard Mandarin.",
        "voice_name": "Gentle Senior",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Crisp_Girl",
        "description": "A warm and crisp young adult female voice in Standard Mandarin.",
        "voice_name": "Crisp Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Pure-hearted_Boy",
        "description": "A committed and pure-hearted young adult male voice in Standard Mandarin.",
        "voice_name": "Pure-hearted Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Soft_Girl",
        "description": "A welcoming and soft adult female voice with a Southern Chinese accent.",
        "voice_name": "Soft Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_IntellectualGirl",
        "description": "An intellectual adult female voice in Standard Mandarin, clear and knowledgeable.",
        "voice_name": "Intellectual Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Warm_HeartedGirl",
        "description": "A warm-hearted and caring adult female voice in Standard Mandarin.",
        "voice_name": "Warm-hearted Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Laid_BackGirl",
        "description": "A relaxed and laid-back adult female voice in Standard Mandarin.",
        "voice_name": "Laid-back Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_ExplorativeGirl",
        "description": "An explorative and curious adult female voice in Standard Mandarin.",
        "voice_name": "Explorative Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_Warm-HeartedAunt",
        "description": "A kind and warm-hearted middle-aged auntie voice in Standard Mandarin.",
        "voice_name": "Warm-hearted Aunt",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Chinese (Mandarin)_BashfulGirl",
        "description": "A bashful and shy female youth voice in Standard Mandarin.",
        "voice_name": "Bashful Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_IntellectualSenior",
        "description": "A mature and intellectual young adult male voice in Japanese, sounding older than his age.",
        "voice_name": "Intellectual Senior",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_DecisivePrincess",
        "description": "A firm and decisive adult princess's voice in Japanese.",
        "voice_name": "Decisive Princess",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_LoyalKnight",
        "description": "A youthful and loyal adult male knight's voice in Japanese.",
        "voice_name": "Loyal Knight",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_DominantMan",
        "description": "A mature and dominant middle-aged male voice in Japanese.",
        "voice_name": "Dominant Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_SeriousCommander",
        "description": "A serious and reliable adult male commander's voice in Japanese.",
        "voice_name": "Serious Commander",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_ColdQueen",
        "description": "A distant and cold adult queen's voice in Japanese.",
        "voice_name": "Cold Queen",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_DependableWoman",
        "description": "A steady and dependable adult female voice in Japanese.",
        "voice_name": "Dependable Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_GentleButler",
        "description": "A charming and gentle adult male butler's voice in Japanese.",
        "voice_name": "Gentle Butler",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_KindLady",
        "description": "A charming and kind adult female voice in Japanese.",
        "voice_name": "Kind Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_CalmLady",
        "description": "A calm and charming adult female voice in Japanese.",
        "voice_name": "Calm Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_OptimisticYouth",
        "description": "A cheerful and optimistic adult male youth's voice in Japanese.",
        "voice_name": "Optimistic Youth",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_GenerousIzakayaOwner",
        "description": "A playful and generous middle-aged male izakaya owner's voice in Standard Japanese.",
        "voice_name": "Generous Izakaya Owner",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_SportyStudent",
        "description": "An inviting and sporty adult male student's voice in Standard Japanese.",
        "voice_name": "Sporty Student",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_InnocentBoy",
        "description": "An inviting and innocent adult male voice in Standard Japanese.",
        "voice_name": "Innocent Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Japanese_GracefulMaiden",
        "description": "A sweet and graceful adult maiden's voice in Standard Japanese.",
        "voice_name": "Graceful Maiden",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Cantonese_ProfessionalHost（F)",
        "description": "A neutral and professional adult female host in Cantonese.",
        "voice_name": "Professional Female Host",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Cantonese_GentleLady",
        "description": "A calm and gentle adult female voice in Cantonese.",
        "voice_name": "Gentle Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Cantonese_ProfessionalHost（M)",
        "description": "A neutral and professional adult male host in Cantonese.",
        "voice_name": "Professional Male Host",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Cantonese_PlayfulMan",
        "description": "A soulful and playful adult male voice in Cantonese.",
        "voice_name": "Playful Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Cantonese_CuteGirl",
        "description": "A soothing and cute young adult female voice in Cantonese.",
        "voice_name": "Cute Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Cantonese_KindWoman",
        "description": "A friendly and kind adult female voice in Cantonese.",
        "voice_name": "Kind Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_AirheadedGirl",
        "description": "A cool and composed adult female voice, suitable for an \"airheaded\" character in Standard Korean.",
        "voice_name": "Airheaded Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_AthleticGirl",
        "description": "A robust and athletic female youth's voice in Standard Korean.",
        "voice_name": "Athletic Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_AthleticStudent",
        "description": "An energetic young adult male athletic student's voice in Standard Korean.",
        "voice_name": "Athletic Student",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_BraveAdventurer",
        "description": "A playful and adventurous adult female brave adventurer's voice in Standard Korean.",
        "voice_name": "Brave Adventurer",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_BraveFemaleWarrior",
        "description": "A resolute young adult brave female warrior's voice in Standard Korean.",
        "voice_name": "Brave Female Warrior",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_BraveYouth",
        "description": "A powerful young adult brave male youth's voice in Standard Korean.",
        "voice_name": "Brave Youth",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_CalmGentleman",
        "description": "A composed and calm middle-aged gentleman's voice in Standard Korean.",
        "voice_name": "Calm Gentleman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_CalmLady",
        "description": "A resilient and determined young adult female voice in Standard Korean.",
        "voice_name": "Calm Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_CaringWoman",
        "description": "A lively and vibrant young adult caring woman's voice in Standard Korean.",
        "voice_name": "Caring Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_CharmingElderSister",
        "description": "A playful and mischievous middle-aged \"charming elder sister\" voice in Standard Korean.",
        "voice_name": "Charming Elder Sister",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_CharmingSister",
        "description": "A seductive middle-aged \"charming sister\" voice in Standard Korean.",
        "voice_name": "Charming Sister",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_CheerfulBoyfriend",
        "description": "A sharp and intense middle-aged male voice in Standard Korean.",
        "voice_name": "Cheerful Boyfriend",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_CheerfulCoolJunior",
        "description": "An energetic and spirited adult male \"cheerful cool junior\" voice in Standard Korean.",
        "voice_name": "Cheerful Cool Junior",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_CheerfulLittleSister",
        "description": "An energetic and lively adult female \"cheerful little sister\" voice in Standard Korean.",
        "voice_name": "Cheerful Little Sister",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_ChildhoodFriendGirl",
        "description": "A polite and reserved young adult female \"childhood friend\" voice in Standard Korean.",
        "voice_name": "Childhood Friend Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_CockyGuy",
        "description": "A playful and mischievous young adult cocky guy's voice in Standard Korean.",
        "voice_name": "Cocky Guy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_ColdGirl",
        "description": "An aloof and cold adult female voice in Standard Korean.",
        "voice_name": "Cold Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_ColdYoungMan",
        "description": "A cold and composed adult male voice in Standard Korean.",
        "voice_name": "Cold Young Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_ConfidentBoss",
        "description": "A deep and commanding middle-aged confident boss's voice in Standard Korean.",
        "voice_name": "Confident Boss",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_ConsiderateSenior",
        "description": "A gentle and mature young adult male \"considerate senior\" voice in Standard Korean.",
        "voice_name": "Considerate Senior",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_DecisiveQueen",
        "description": "A sweet yet resolute young adult decisive queen's voice in Standard Korean.",
        "voice_name": "Decisive Queen",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_DominantMan",
        "description": "A mature and authoritative dominant adult male voice in Standard Korean.",
        "voice_name": "Dominant Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_ElegantPrincess",
        "description": "A graceful and refined adult princess voice in Standard Korean.",
        "voice_name": "Elegant Princess",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_EnchantingSister",
        "description": "A desirable and charming young adult \"enchanting sister\" voice in Standard Korean.",
        "voice_name": "Enchanting Sister",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_EnthusiasticTeen",
        "description": "A passionate and lively young adult male teen's voice in Standard Korean.",
        "voice_name": "Enthusiastic Teen",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_FriendlyBigSister",
        "description": "A charismatic and alluring middle-aged \"friendly big sister\" voice in Standard Korean.",
        "voice_name": "Friendly Big Sister",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_GentleBoss",
        "description": "A regal and refined middle-aged male \"gentle boss\" voice in Standard Korean.",
        "voice_name": "Gentle Boss",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_GentleWoman",
        "description": "A strong-willed yet gentle young adult female voice in Standard Korean.",
        "voice_name": "Gentle Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_HaughtyLady",
        "description": "A cold and distant young adult haughty lady's voice in Standard Korean.",
        "voice_name": "Haughty Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_InnocentBoy",
        "description": "A naive and pure young adult male \"innocent boy\" voice in Standard Korean.",
        "voice_name": "Innocent Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_IntellectualMan",
        "description": "A combative middle-aged intellectual male voice in Standard Korean.",
        "voice_name": "Intellectual Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_IntellectualSenior",
        "description": "A magnetic and intellectual young adult male voice with a senior quality in Standard Korean.",
        "voice_name": "Intellectual Senior",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_LonelyWarrior",
        "description": "A youthful and daring adult male \"lonely warrior\" voice in Standard Korean.",
        "voice_name": "Lonely Warrior",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_MatureLady",
        "description": "A refined and elegant mature middle-aged lady's voice in Standard Korean.",
        "voice_name": "Mature Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_MysteriousGirl",
        "description": "An energetic and lively female youth voice for a mysterious character in Standard Korean.",
        "voice_name": "Mysterious Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_OptimisticYouth",
        "description": "A cheerful and optimistic young adult male youth's voice in Standard Korean.",
        "voice_name": "Optimistic Youth",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_PlayboyCharmer",
        "description": "A seductive young adult male \"playboy charmer\" voice in Standard Korean.",
        "voice_name": "Playboy Charmer",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_PossessiveMan",
        "description": "A powerful and authoritative middle-aged possessive man's voice in Standard Korean.",
        "voice_name": "Possessive Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_QuirkyGirl",
        "description": "An adorable and quirky female youth voice in Standard Korean.",
        "voice_name": "Quirky Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_ReliableSister",
        "description": "A powerful and authoritative middle-aged \"reliable sister\" voice in Standard Korean.",
        "voice_name": "Reliable Sister",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_ReliableYouth",
        "description": "A gentle and considerate young adult reliable male youth's voice in Standard Korean.",
        "voice_name": "Reliable Youth",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_SassyGirl",
        "description": "A Sassy female youth voice in Standard Korean.",
        "voice_name": "Sassy Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_ShyGirl",
        "description": "A timid and introverted young adult female voice in Standard Korean.",
        "voice_name": "Shy Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_SoothingLady",
        "description": "An alluring and soothing middle-aged female voice in Standard Korean.",
        "voice_name": "Soothing Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_StrictBoss",
        "description": "A stern middle-aged male boss's voice in Standard Korean.",
        "voice_name": "Strict Boss",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_SweetGirl",
        "description": "A soothing and gentle middle-aged female voice in Standard Korean, sweet and calming.",
        "voice_name": "Sweet Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_ThoughtfulWoman",
        "description": "A mature and contemplative young adult thoughtful woman's voice in Standard Korean.",
        "voice_name": "Thoughtful Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_WiseElf",
        "description": "A sweet and ethereal young adult female \"wise elf\" voice in Standard Korean.",
        "voice_name": "Wise Elf",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Korean_WiseTeacher",
        "description": "A sagacious and wise middle-aged male teacher's voice in Standard Korean.",
        "voice_name": "Wise Teacher",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_SereneWoman",
        "description": "A soothing and serene young adult female voice in Standard Spanish.",
        "voice_name": "Serene Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_MaturePartner",
        "description": "A warm and mature middle-aged male partner's voice in Standard Spanish.",
        "voice_name": "Mature Partner",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_CaptivatingStoryteller",
        "description": "A captivating middle-aged male narrator's voice in Standard Spanish, perfect for storytelling.",
        "voice_name": "Captivating Storyteller",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Narrator",
        "description": "A middle-aged female narrator's voice in Standard Spanish, ideal for storytelling.",
        "voice_name": "Narrator",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_WiseScholar",
        "description": "A conversational young adult male wise scholar's voice in Standard Spanish.",
        "voice_name": "Wise Scholar",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Kind-heartedGirl",
        "description": "A bright and kind-hearted young adult female voice in Standard Spanish.",
        "voice_name": "Kind-hearted Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_DeterminedManager",
        "description": "A businesslike and determined middle-aged female manager's voice in Standard Spanish.",
        "voice_name": "Determined Manager",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_BossyLeader",
        "description": "A businesslike and bossy adult male leader's voice in Standard Spanish.",
        "voice_name": "Bossy Leader",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_ReservedYoungMan",
        "description": "A tranquil and reserved young adult male voice in Standard Spanish.",
        "voice_name": "Reserved Young Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_ConfidentWoman",
        "description": "A clear and firm young adult confident woman's voice in Standard Spanish.",
        "voice_name": "Confident Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_ThoughtfulMan",
        "description": "A sober and thoughtful young adult male voice in Standard Spanish.",
        "voice_name": "Thoughtful Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Strong-WilledBoy",
        "description": "A mature and strong-willed adult male voice in Standard Spanish.",
        "voice_name": "Strong-willed Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_SophisticatedLady",
        "description": "A refined and sophisticated adult lady's voice in Standard Spanish.",
        "voice_name": "Sophisticated Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_RationalMan",
        "description": "A thoughtful and rational adult male voice in Standard Spanish.",
        "voice_name": "Rational Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_AnimeCharacter",
        "description": "An animated middle-aged female voice in Standard Spanish, suitable for anime characters.",
        "voice_name": "Anime Character",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Deep-tonedMan",
        "description": "A charismatic, deep-toned middle-aged male voice in Standard Spanish.",
        "voice_name": "Deep-toned Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Fussyhostess",
        "description": "An intense and fussy middle-aged female hostess's voice in Standard Spanish.",
        "voice_name": "Fussy hostess",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_SincereTeen",
        "description": "A heartfelt and sincere male teen's voice in Standard Spanish.",
        "voice_name": "Sincere Teen",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_FrankLady",
        "description": "An agitated and frank adult lady's voice in Standard Spanish.",
        "voice_name": "Frank Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Comedian",
        "description": "A humorous young adult male comedian's voice in Standard Spanish.",
        "voice_name": "Comedian",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Debator",
        "description": "A tough middle-aged male debater's voice in Standard Spanish.",
        "voice_name": "Debator",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_ToughBoss",
        "description": "A mature and tough middle-aged female boss's voice in Standard Spanish.",
        "voice_name": "Tough Boss",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Wiselady",
        "description": "A neutral and wise middle-aged lady's voice in Standard Spanish.",
        "voice_name": "Wise Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Steadymentor",
        "description": "An arrogant yet steady young adult male mentor's voice in Standard Spanish.",
        "voice_name": "Steady Mentor",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Jovialman",
        "description": "A gravelly and jovial senior male voice in Standard Spanish.",
        "voice_name": "Jovial Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_SantaClaus",
        "description": "A joyful senior male Santa Claus voice in Standard Spanish.",
        "voice_name": "Santa Claus",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Rudolph",
        "description": "A naive young adult male voice in the style of Rudolph in Standard Spanish.",
        "voice_name": "Rudolph",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Intonategirl",
        "description": "A versatile young adult female voice in Standard Spanish.",
        "voice_name": "Intonate Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Arnold",
        "description": "A steady adult male voice in the style of Arnold in Standard Spanish.",
        "voice_name": "Arnold",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_Ghost",
        "description": "A raspy adult male ghost's voice in Standard Spanish.",
        "voice_name": "Ghost",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_HumorousElder",
        "description": "An eccentric and humorous senior male elder's voice in Standard Spanish.",
        "voice_name": "Humorous Elder",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_EnergeticBoy",
        "description": "A cheerful and energetic young adult male voice in Standard Spanish.",
        "voice_name": "Energetic Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_WhimsicalGirl",
        "description": "A witty and whimsical young adult female voice in Standard Spanish.",
        "voice_name": "Whimsical Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_StrictBoss",
        "description": "A commanding and strict young adult female boss's voice in Standard Spanish.",
        "voice_name": "Strict Boss",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_ReliableMan",
        "description": "A steady and reliable adult male voice in Standard Spanish.",
        "voice_name": "Reliable Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_SereneElder",
        "description": "A reflective and serene senior male elder's voice in Standard Spanish.",
        "voice_name": "Serene Elder",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_AngryMan",
        "description": "An intense young adult male voice in Standard Spanish, conveying anger.",
        "voice_name": "Angry Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_AssertiveQueen",
        "description": "A firm and assertive young adult queen's voice in Standard Spanish.",
        "voice_name": "Assertive Queen",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_CaringGirlfriend",
        "description": "A dreamy adult female caring girlfriend's voice in Standard Spanish.",
        "voice_name": "Caring Girlfriend",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_PowerfulSoldier",
        "description": "A youthful and bold young adult male powerful soldier's voice in Standard Spanish.",
        "voice_name": "Powerful Soldier",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_PassionateWarrior",
        "description": "An energetic and passionate young adult male warrior's voice in Standard Spanish.",
        "voice_name": "Passionate Warrior",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_ChattyGirl",
        "description": "A conversational and chatty young adult female voice in Standard Spanish.",
        "voice_name": "Chatty Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_RomanticHusband",
        "description": "An emotional middle-aged male romantic husband's voice in Standard Spanish.",
        "voice_name": "Romantic Husband",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_CompellingGirl",
        "description": "A persuasive and compelling young adult female voice in Standard Spanish.",
        "voice_name": "Compelling Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_PowerfulVeteran",
        "description": "A strong and powerful middle-aged male veteran's voice in Standard Spanish.",
        "voice_name": "Powerful Veteran",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_SensibleManager",
        "description": "A charismatic and sensible adult male manager's voice in Standard Spanish.",
        "voice_name": "Sensible Manager",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Spanish_ThoughtfulLady",
        "description": "A worried and thoughtful adult lady's voice in Standard Spanish.",
        "voice_name": "Thoughtful Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_SentimentalLady",
        "description": "An elegant and sentimental young adult female voice in Portuguese.",
        "voice_name": "Sentimental Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_BossyLeader",
        "description": "A calm and formal adult male bossy leader's voice in Portuguese.",
        "voice_name": "Bossy Leader",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Wiselady",
        "description": "A smooth and wise middle-aged lady's voice in Portuguese.",
        "voice_name": "Wise lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Strong-WilledBoy",
        "description": "A mature and strong-willed young adult male voice in Portuguese.",
        "voice_name": "Strong-willed Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Deep-VoicedGentleman",
        "description": "A deep-voiced adult gentleman in Portuguese.",
        "voice_name": "Deep-voiced Gentleman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_UpsetGirl",
        "description": "A sad young adult female voice in Portuguese, conveying upset emotions.",
        "voice_name": "Upset Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_PassionateWarrior",
        "description": "An energetic and passionate young adult male warrior's voice in Portuguese.",
        "voice_name": "Passionate Warrior",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_AnimeCharacter",
        "description": "An animated middle-aged female voice in Portuguese, suitable for anime characters.",
        "voice_name": "Anime Character",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_ConfidentWoman",
        "description": "A clear and firm young adult confident woman's voice in Portuguese.",
        "voice_name": "Confident Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_AngryMan",
        "description": "A serious young adult male voice in Portuguese, conveying anger.",
        "voice_name": "Angry Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_CaptivatingStoryteller",
        "description": "A captivating middle-aged male narrator's voice in Portuguese, ideal for storytelling.",
        "voice_name": "Captivating Storyteller",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Godfather",
        "description": "A serious middle-aged male godfather voice in Standard Portuguese, conveying authority.",
        "voice_name": "Godfather",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_ReservedYoungMan",
        "description": "A cold and calm reserved young adult male voice in Standard Portuguese.",
        "voice_name": "Reserved Young Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_SmartYoungGirl",
        "description": "An intelligent young female girl's voice in Standard Portuguese, sharp and clear.",
        "voice_name": "Smart Young Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Kind-heartedGirl",
        "description": "A calm and kind-hearted young adult female voice in Standard Portuguese.",
        "voice_name": "Kind-hearted Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Pompouslady",
        "description": "A pompous young adult female cartoon-style voice in Standard Portuguese, full of personality.",
        "voice_name": "Pompous lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Grinch",
        "description": "A cunning adult male Grinch-like voice in Standard Portuguese, mischievous and sly.",
        "voice_name": "Grinch",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Debator",
        "description": "A tough middle-aged male debater's voice in Standard Portuguese, strong and assertive.",
        "voice_name": "Debator",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_SweetGirl",
        "description": "An adorable and sweet young adult female voice in Standard Portuguese.",
        "voice_name": "Sweet Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_AttractiveGirl",
        "description": "An alluring and attractive adult female voice in Standard Portuguese.",
        "voice_name": "Attractive Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_ThoughtfulMan",
        "description": "A gentle and thoughtful young adult male voice in Standard Portuguese.",
        "voice_name": "Thoughtful Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_PlayfulGirl",
        "description": "A cutesy and playful female youth voice in Standard Portuguese.",
        "voice_name": "Playful Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_GorgeousLady",
        "description": "A playful and gorgeous adult female voice in Standard Portuguese, exuding confidence.",
        "voice_name": "Gorgeous Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_LovelyLady",
        "description": "A charismatic and lovely adult female voice in Standard Portuguese.",
        "voice_name": "Lovely Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_SereneWoman",
        "description": "A calm and serene young adult female voice in Standard Portuguese, peaceful and composed.",
        "voice_name": "Serene Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_SadTeen",
        "description": "A frustrated and sad male teen's voice in Standard Portuguese.",
        "voice_name": "Sad Teen",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_MaturePartner",
        "description": "A mature middle-aged male partner's voice in Standard Portuguese, dependable and warm.",
        "voice_name": "Mature Partner",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Comedian",
        "description": "A humorous young adult male comedian's voice in Standard Portuguese.",
        "voice_name": "Comedian",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_NaughtySchoolgirl",
        "description": "An inviting and naughty young adult female schoolgirl's voice in Standard Portuguese.",
        "voice_name": "Naughty Schoolgirl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Narrator",
        "description": "A middle-aged female narrator's voice in Standard Portuguese, perfect for storytelling.",
        "voice_name": "Narrator",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_ToughBoss",
        "description": "A mature and tough middle-aged female boss's voice in Standard Portuguese.",
        "voice_name": "Tough Boss",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Fussyhostess",
        "description": "An intense and fussy middle-aged female hostess's voice in Standard Portuguese.",
        "voice_name": "Fussy hostess",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Dramatist",
        "description": "A quirky middle-aged male dramatist's voice in Standard Portuguese.",
        "voice_name": "Dramatist",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Steadymentor",
        "description": "An arrogant yet steady young adult male mentor's voice in Standard Portuguese.",
        "voice_name": "Steady Mentor",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Jovialman",
        "description": "A jovial and laughing middle-aged male voice in Standard Portuguese.",
        "voice_name": "Jovial Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_CharmingQueen",
        "description": "A bewitching and charming adult queen's voice in Standard Portuguese.",
        "voice_name": "Charming Queen",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_SantaClaus",
        "description": "A joyful middle-aged male Santa Claus voice in Standard Portuguese, full of holiday cheer.",
        "voice_name": "Santa Claus",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Rudolph",
        "description": "A naive young adult female voice in the style of Rudolph in Standard Portuguese.",
        "voice_name": "Rudolph",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Arnold",
        "description": "A steady adult male voice in the style of Arnold in Standard Portuguese, strong and firm.",
        "voice_name": "Arnold",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_CharmingSanta",
        "description": "An attractive and charming middle-aged male Santa voice in Standard Portuguese.",
        "voice_name": "Charming Santa",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_CharmingLady",
        "description": [],
        "voice_name": "Charming Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Ghost",
        "description": "A sensual adult male ghost's voice in Standard Portuguese, mysterious and alluring.",
        "voice_name": "Ghost",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_HumorousElder",
        "description": "A wacky and humorous middle-aged male elder's voice in Standard Portuguese.",
        "voice_name": "Humorous Elder",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_CalmLeader",
        "description": "A composed and calm middle-aged male leader's voice in Standard Portuguese.",
        "voice_name": "Calm Leader",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_GentleTeacher",
        "description": "A mild and gentle adult male teacher's voice in Standard Portuguese.",
        "voice_name": "Gentle Teacher",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_EnergeticBoy",
        "description": "A cheerful and energetic young adult male voice in Standard Portuguese.",
        "voice_name": "Energetic Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_ReliableMan",
        "description": "A steady and reliable adult male voice in Standard Portuguese.",
        "voice_name": "Reliable Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_SereneElder",
        "description": "A reflective and serene middle-aged male elder's voice in Standard Portuguese.",
        "voice_name": "Serene Elder",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_GrimReaper",
        "description": "A sinister adult male Grim Reaper's voice in Standard Portuguese, dark and ominous.",
        "voice_name": "Grim Reaper",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_AssertiveQueen",
        "description": "A firm and assertive young adult queen's voice in Standard Portuguese.",
        "voice_name": "Assertive Queen",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_WhimsicalGirl",
        "description": "A lovely and whimsical young adult female voice in Standard Portuguese.",
        "voice_name": "Whimsical Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_StressedLady",
        "description": "An unsure and stressed middle-aged lady's voice in Standard Portuguese.",
        "voice_name": "Stressed Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_FriendlyNeighbor",
        "description": "An energetic and friendly young adult female neighbor's voice in Standard Portuguese.",
        "voice_name": "Friendly Neighbor",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_CaringGirlfriend",
        "description": "A dreamy middle-aged female caring girlfriend's voice in Standard Portuguese.",
        "voice_name": "Caring Girlfriend",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_PowerfulSoldier",
        "description": "A youthful and bold young adult male powerful soldier's voice in Standard Portuguese.",
        "voice_name": "Powerful Soldier",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_FascinatingBoy",
        "description": "An approachable and fascinating young adult male voice in Standard Portuguese.",
        "voice_name": "Fascinating Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_RomanticHusband",
        "description": "An emotional middle-aged male romantic husband's voice in Standard Portuguese.",
        "voice_name": "Romantic Husband",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_StrictBoss",
        "description": "A robotic and strict young adult female boss's voice in Standard Portuguese.",
        "voice_name": "Strict Boss",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_InspiringLady",
        "description": "A commanding and inspiring young adult female voice in Standard Portuguese.",
        "voice_name": "Inspiring Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_PlayfulSpirit",
        "description": "An animated and playful young adult female spirit's voice in Standard Portuguese.",
        "voice_name": "Playful Spirit",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_ElegantGirl",
        "description": "A dramatic and elegant young adult female voice in Standard Portuguese.",
        "voice_name": "Elegant Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_CompellingGirl",
        "description": "A persuasive and compelling young adult female voice in Standard Portuguese.",
        "voice_name": "Compelling Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_PowerfulVeteran",
        "description": "A strong and powerful middle-aged male veteran's voice in Standard Portuguese.",
        "voice_name": "Powerful Veteran",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_SensibleManager",
        "description": "A charismatic and sensible middle-aged male manager's voice in Standard Portuguese.",
        "voice_name": "Sensible Manager",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_ThoughtfulLady",
        "description": "A worried and thoughtful middle-aged lady's voice in Standard Portuguese.",
        "voice_name": "Thoughtful Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_TheatricalActor",
        "description": "An animated middle-aged male theatrical actor's voice in Standard Portuguese.",
        "voice_name": "Theatrical Actor",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_FragileBoy",
        "description": "A gentle and fragile young adult male voice in Standard Portuguese.",
        "voice_name": "Fragile Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_ChattyGirl",
        "description": "A conversational and chatty young adult female voice in Standard Portuguese.",
        "voice_name": "Chatty Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_Conscientiousinstructor",
        "description": "A youthful and conscientious young adult female instructor's voice in Standard Portuguese.",
        "voice_name": "Conscientious Instructor",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_RationalMan",
        "description": "A thoughtful and rational adult male voice in Standard Portuguese.",
        "voice_name": "Rational Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_WiseScholar",
        "description": "A conversational young adult male wise scholar's voice in Standard Portuguese.",
        "voice_name": "Wise Scholar",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_FrankLady",
        "description": "An agitated and frank middle-aged lady's voice in Standard Portuguese.",
        "voice_name": "Frank Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Portuguese_DeterminedManager",
        "description": "A middle-aged female manager's voice with attitude and determination in Standard Portuguese.",
        "voice_name": "Determined Manager",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "French_Male_Speech_New",
        "description": "A level-headed and composed adult male voice in French.",
        "voice_name": "Level-Headed Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "French_Female_News Anchor",
        "description": "A patient adult female presenter in French, calm and clear.",
        "voice_name": "Patient Female Presenter",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "French_CasualMan",
        "description": "A casual and relaxed middle-aged male voice in French.",
        "voice_name": "Casual Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "French_MovieLeadFemale",
        "description": "A cinematic young adult female lead voice in French, perfect for film.",
        "voice_name": "Movie Lead Female",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "French_FemaleAnchor",
        "description": "A professional adult female anchor voice in French, authoritative and clear.",
        "voice_name": "Female Anchor",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "French_MaleNarrator",
        "description": "A classic adult male narrator voice in French, ideal for storytelling.",
        "voice_name": "Male Narrator",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Indonesian_SweetGirl",
        "description": "A cute and sweet young adult female voice in Indonesian.",
        "voice_name": "Sweet Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Indonesian_ReservedYoungMan",
        "description": "A cold and reserved young adult male voice in Indonesian.",
        "voice_name": "Reserved Young Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Indonesian_CharmingGirl",
        "description": "An alluring and charming adult female voice in Indonesian.",
        "voice_name": "Charming Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Indonesian_CalmWoman",
        "description": "A serene and calm young adult female voice in Indonesian.",
        "voice_name": "Calm Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Indonesian_ConfidentWoman",
        "description": "An assertive and confident young adult female voice in Indonesian.",
        "voice_name": "Confident Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Indonesian_CaringMan",
        "description": "A compassionate and caring young adult male voice in Indonesian.",
        "voice_name": "Caring Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Indonesian_BossyLeader",
        "description": "A calm, authoritative, and bossy adult male leader's voice in Indonesian.",
        "voice_name": "Bossy Leader",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Indonesian_DeterminedBoy",
        "description": "A mature and resolute young adult male voice in Indonesian, conveying determination.",
        "voice_name": "Determined Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Indonesian_GentleGirl",
        "description": "A soft-spoken and gentle young adult female voice in Indonesian.",
        "voice_name": "Gentle Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "German_FriendlyMan",
        "description": "A sincere and friendly middle-aged male voice in German.",
        "voice_name": "Friendly Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "German_SweetLady",
        "description": "An animated and sweet adult female voice in German.",
        "voice_name": "Sweet Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "German_PlayfulMan",
        "description": "A lively and spirited adult male voice in German, full of energy.",
        "voice_name": "Playful Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Russian_HandsomeChildhoodFriend",
        "description": "An aggressive female youth's voice for a handsome childhood friend character in Standard Russian.",
        "voice_name": "Handsome Childhood Friend",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Russian_BrightHeroine",
        "description": "An arrogant and bright adult queen's voice in Standard Russian.",
        "voice_name": "Bright Queen",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Russian_AmbitiousWoman",
        "description": "A demanding and ambitious adult woman's voice in Standard Russian.",
        "voice_name": "Ambitious Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Russian_ReliableMan",
        "description": "A steady and reliable middle-aged man's voice in Standard Russian.",
        "voice_name": "Reliable Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Russian_CrazyQueen",
        "description": "An energetic adult female \"crazy girl\" voice in Standard Russian, wild and unpredictable.",
        "voice_name": "Crazy Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Russian_PessimisticGirl",
        "description": "A compassionate adult female \"pessimistic girl\" voice in Standard Russian.",
        "voice_name": "Pessimistic Girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Russian_AttractiveGuy",
        "description": "A deep-voiced and attractive adult guy's voice in Standard Russian.",
        "voice_name": "Attractive Guy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Russian_Bad-temperedBoy",
        "description": "A charming adult male \"bad-tempered boy\" voice in Standard Russian.",
        "voice_name": "Bad-tempered Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Italian_BraveHeroine",
        "description": "A calm and brave middle-aged female heroine's voice in Italian.",
        "voice_name": "Brave Heroine",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Italian_Narrator",
        "description": "A classic middle-aged male narrator voice in Italian.",
        "voice_name": "Narrator",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Italian_WanderingSorcerer",
        "description": "A ruthless adult female wandering sorcerer's voice in Italian.",
        "voice_name": "Wandering Sorcerer",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Italian_DiligentLeader",
        "description": "A calm and diligent adult female leader's voice in Italian.",
        "voice_name": "Diligent Leader",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Dutch_kindhearted_girl",
        "description": "A warm and kind-hearted young adult female voice in Dutch.",
        "voice_name": "Kind-hearted girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Dutch_bossy_leader",
        "description": "A serious and bossy adult male leader's voice in Dutch.",
        "voice_name": "Bossy leader",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Vietnamese_kindhearted_girl",
        "description": "A warm and kind-hearted young adult female voice in Vietnamese.",
        "voice_name": "Kind-hearted girl",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Arabic_CalmWoman",
        "description": "A calm adult female Arabic voice, ideal for audiobooks and serene narration.",
        "voice_name": "Calm Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Arabic_FriendlyGuy",
        "description": "A natural and friendly adult male Arabic voice.",
        "voice_name": "Friendly Guy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Turkish_CalmWoman",
        "description": "A calm adult female Turkish voice, ideal for audiobooks.",
        "voice_name": "Calm Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Turkish_Trustworthyman",
        "description": "A resonant and trustworthy adult male Turkish voice.",
        "voice_name": "Trustworthy man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Ukrainian_CalmWoman",
        "description": "A calm adult female Ukrainian voice, ideal for audiobooks.",
        "voice_name": "Calm Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Ukrainian_WiseScholar",
        "description": "A conversational young adult male wise scholar's voice in Ukrainian.",
        "voice_name": "Wise Scholar",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Thai_male_1_sample8",
        "description": "A magnetic and serene adult male voice in Thai.",
        "voice_name": "Serene Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Thai_male_2_sample2",
        "description": "A lively and friendly adult male voice in Thai.",
        "voice_name": "Friendly Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Thai_female_1_sample1",
        "description": "A neutral and confident adult female voice in Thai.",
        "voice_name": "Confident Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Thai_female_2_sample2",
        "description": "An energetic adult female voice in Thai.",
        "voice_name": "Energetic Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Polish_male_1_sample4",
        "description": "A mature adult male narrator's voice in Polish.",
        "voice_name": "Male Narrator",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Polish_male_2_sample3",
        "description": "An adult male broadcast anchor's voice in Polish.",
        "voice_name": "Male Anchor",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Polish_female_1_sample1",
        "description": "A calm adult female voice in Polish.",
        "voice_name": "Calm Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Polish_female_2_sample3",
        "description": "A neutral and casual adult female voice in Polish.",
        "voice_name": "Casual Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Romanian_male_1_sample2",
        "description": "A neutral and reliable adult male voice in Romanian.",
        "voice_name": "Reliable Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Romanian_male_2_sample1",
        "description": "An energetic adult male youth's voice in Romanian.",
        "voice_name": "Energetic Youth",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Romanian_female_1_sample4",
        "description": "A cheerful and optimistic adult female youth's voice in Romanian.",
        "voice_name": "Optimistic Youth",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Romanian_female_2_sample1",
        "description": "A gentle adult female voice in Romanian.",
        "voice_name": "Gentle Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "greek_male_1a_v1",
        "description": "An intellectual and thoughtful adult male mentor's voice in Greek.",
        "voice_name": "Thoughtful Mentor",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Greek_female_1_sample1",
        "description": "A gentle adult lady's voice in Greek.",
        "voice_name": "Gentle Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "Greek_female_2_sample3",
        "description": "A cheerful young adult \"girl next door\" voice in Greek.",
        "voice_name": "Girl Next Door",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "czech_male_1_v1",
        "description": "A serious and assured young adult male presenter's voice in Czech.",
        "voice_name": "Assured Presenter",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "czech_female_5_v7",
        "description": "A steadfast adult female broadcast narrator's voice in Czech.",
        "voice_name": "Steadfast Narrator",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "czech_female_2_v2",
        "description": "A graceful and elegant adult lady's voice in Czech.",
        "voice_name": "Elegant Lady",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "finnish_male_3_v1",
        "description": "An energetic and upbeat young adult female voice in Finnish.",
        "voice_name": "Upbeat Man",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "finnish_male_1_v2",
        "description": "A deep and friendly young adult male voice in Finnish.",
        "voice_name": "Friendly Boy",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "finnish_female_4_v1",
        "description": "A determined and assertive adult female voice in Finnish.",
        "voice_name": "Assetive Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "hindi_male_1_v2",
        "description": "A magnetic and trustworthy adult male advisor's voice in Hindi.",
        "voice_name": "Trustworthy Advisor",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "hindi_female_2_v1",
        "description": "A gentle and tranquil adult female voice in Hindi.",
        "voice_name": "Tranquil Woman",
        "created_time": "2025-01-01"
    },
    {
        "voice_id": "hindi_female_1_v2",
        "description": "A calm adult female news anchor's voice in Hindi.",
        "voice_name": "News Anchor",
        "created_time": "2025-01-01"
    }
]


@app.get("/get_voice_models")
async def get_voice_models(request: Request):
    pass





