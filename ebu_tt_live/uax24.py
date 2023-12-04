"""Utility for discovering which UAX24 script a given character code is in,
useful for example in computing the copy or render times in the IMSC-HRM.

Auto-generated from UAX24 Scripts.txt using gen_uax24.py
"""
def lr(a, b):
    return list(range(a, b))


Common_list = [
    *lr(0x0000, 0x001F),
    0x0020,
    *lr(0x0021, 0x0023),
    0x0024,
    *lr(0x0025, 0x0027),
    0x0028,
    0x0029,
    0x002A,
    0x002B,
    0x002C,
    0x002D,
    *lr(0x002E, 0x002F),
    *lr(0x0030, 0x0039),
    *lr(0x003A, 0x003B),
    *lr(0x003C, 0x003E),
    *lr(0x003F, 0x0040),
    0x005B,
    0x005C,
    0x005D,
    0x005E,
    0x005F,
    0x0060,
    0x007B,
    0x007C,
    0x007D,
    0x007E,
    *lr(0x007F, 0x009F),
    0x00A0,
    0x00A1,
    *lr(0x00A2, 0x00A5),
    0x00A6,
    0x00A7,
    0x00A8,
    0x00A9,
    0x00AB,
    0x00AC,
    0x00AD,
    0x00AE,
    0x00AF,
    0x00B0,
    0x00B1,
    *lr(0x00B2, 0x00B3),
    0x00B4,
    0x00B5,
    *lr(0x00B6, 0x00B7),
    0x00B8,
    0x00B9,
    0x00BB,
    *lr(0x00BC, 0x00BE),
    0x00BF,
    0x00D7,
    0x00F7,
    *lr(0x02B9, 0x02C1),
    *lr(0x02C2, 0x02C5),
    *lr(0x02C6, 0x02D1),
    *lr(0x02D2, 0x02DF),
    *lr(0x02E5, 0x02E9),
    0x02EC,
    0x02ED,
    0x02EE,
    *lr(0x02EF, 0x02FF),
    0x0374,
    0x037E,
    0x0385,
    0x0387,
    0x0605,
    0x060C,
    0x061B,
    0x061F,
    0x0640,
    0x06DD,
    0x08E2,
    *lr(0x0964, 0x0965),
    0x0E3F,
    *lr(0x0FD5, 0x0FD8),
    0x10FB,
    *lr(0x16EB, 0x16ED),
    *lr(0x1735, 0x1736),
    *lr(0x1802, 0x1803),
    0x1805,
    0x1CD3,
    0x1CE1,
    *lr(0x1CE9, 0x1CEC),
    *lr(0x1CEE, 0x1CF3),
    *lr(0x1CF5, 0x1CF6),
    0x1CF7,
    0x1CFA,
    *lr(0x2000, 0x200A),
    0x200B,
    *lr(0x200E, 0x200F),
    *lr(0x2010, 0x2015),
    *lr(0x2016, 0x2017),
    0x2018,
    0x2019,
    0x201A,
    *lr(0x201B, 0x201C),
    0x201D,
    0x201E,
    0x201F,
    *lr(0x2020, 0x2027),
    0x2028,
    0x2029,
    *lr(0x202A, 0x202E),
    0x202F,
    *lr(0x2030, 0x2038),
    0x2039,
    0x203A,
    *lr(0x203B, 0x203E),
    *lr(0x203F, 0x2040),
    *lr(0x2041, 0x2043),
    0x2044,
    0x2045,
    0x2046,
    *lr(0x2047, 0x2051),
    0x2052,
    0x2053,
    0x2054,
    *lr(0x2055, 0x205E),
    0x205F,
    *lr(0x2060, 0x2064),
    *lr(0x2066, 0x206F),
    0x2070,
    *lr(0x2074, 0x2079),
    *lr(0x207A, 0x207C),
    0x207D,
    0x207E,
    *lr(0x2080, 0x2089),
    *lr(0x208A, 0x208C),
    0x208D,
    0x208E,
    *lr(0x20A0, 0x20C0),
    *lr(0x2100, 0x2101),
    0x2102,
    *lr(0x2103, 0x2106),
    0x2107,
    *lr(0x2108, 0x2109),
    *lr(0x210A, 0x2113),
    0x2114,
    0x2115,
    *lr(0x2116, 0x2117),
    0x2118,
    *lr(0x2119, 0x211D),
    *lr(0x211E, 0x2123),
    0x2124,
    0x2125,
    0x2127,
    0x2128,
    0x2129,
    *lr(0x212C, 0x212D),
    0x212E,
    *lr(0x212F, 0x2131),
    *lr(0x2133, 0x2134),
    *lr(0x2135, 0x2138),
    0x2139,
    *lr(0x213A, 0x213B),
    *lr(0x213C, 0x213F),
    *lr(0x2140, 0x2144),
    *lr(0x2145, 0x2149),
    0x214A,
    0x214B,
    *lr(0x214C, 0x214D),
    0x214F,
    *lr(0x2150, 0x215F),
    0x2189,
    *lr(0x218A, 0x218B),
    *lr(0x2190, 0x2194),
    *lr(0x2195, 0x2199),
    *lr(0x219A, 0x219B),
    *lr(0x219C, 0x219F),
    0x21A0,
    *lr(0x21A1, 0x21A2),
    0x21A3,
    *lr(0x21A4, 0x21A5),
    0x21A6,
    *lr(0x21A7, 0x21AD),
    0x21AE,
    *lr(0x21AF, 0x21CD),
    *lr(0x21CE, 0x21CF),
    *lr(0x21D0, 0x21D1),
    0x21D2,
    0x21D3,
    0x21D4,
    *lr(0x21D5, 0x21F3),
    *lr(0x21F4, 0x22FF),
    *lr(0x2300, 0x2307),
    0x2308,
    0x2309,
    0x230A,
    0x230B,
    *lr(0x230C, 0x231F),
    *lr(0x2320, 0x2321),
    *lr(0x2322, 0x2328),
    0x2329,
    0x232A,
    *lr(0x232B, 0x237B),
    0x237C,
    *lr(0x237D, 0x239A),
    *lr(0x239B, 0x23B3),
    *lr(0x23B4, 0x23DB),
    *lr(0x23DC, 0x23E1),
    *lr(0x23E2, 0x2426),
    *lr(0x2440, 0x244A),
    *lr(0x2460, 0x249B),
    *lr(0x249C, 0x24E9),
    *lr(0x24EA, 0x24FF),
    *lr(0x2500, 0x25B6),
    0x25B7,
    *lr(0x25B8, 0x25C0),
    0x25C1,
    *lr(0x25C2, 0x25F7),
    *lr(0x25F8, 0x25FF),
    *lr(0x2600, 0x266E),
    0x266F,
    *lr(0x2670, 0x2767),
    0x2768,
    0x2769,
    0x276A,
    0x276B,
    0x276C,
    0x276D,
    0x276E,
    0x276F,
    0x2770,
    0x2771,
    0x2772,
    0x2773,
    0x2774,
    0x2775,
    *lr(0x2776, 0x2793),
    *lr(0x2794, 0x27BF),
    *lr(0x27C0, 0x27C4),
    0x27C5,
    0x27C6,
    *lr(0x27C7, 0x27E5),
    0x27E6,
    0x27E7,
    0x27E8,
    0x27E9,
    0x27EA,
    0x27EB,
    0x27EC,
    0x27ED,
    0x27EE,
    0x27EF,
    *lr(0x27F0, 0x27FF),
    *lr(0x2900, 0x2982),
    0x2983,
    0x2984,
    0x2985,
    0x2986,
    0x2987,
    0x2988,
    0x2989,
    0x298A,
    0x298B,
    0x298C,
    0x298D,
    0x298E,
    0x298F,
    0x2990,
    0x2991,
    0x2992,
    0x2993,
    0x2994,
    0x2995,
    0x2996,
    0x2997,
    0x2998,
    *lr(0x2999, 0x29D7),
    0x29D8,
    0x29D9,
    0x29DA,
    0x29DB,
    *lr(0x29DC, 0x29FB),
    0x29FC,
    0x29FD,
    *lr(0x29FE, 0x2AFF),
    *lr(0x2B00, 0x2B2F),
    *lr(0x2B30, 0x2B44),
    *lr(0x2B45, 0x2B46),
    *lr(0x2B47, 0x2B4C),
    *lr(0x2B4D, 0x2B73),
    *lr(0x2B76, 0x2B95),
    *lr(0x2B97, 0x2BFF),
    *lr(0x2E00, 0x2E01),
    0x2E02,
    0x2E03,
    0x2E04,
    0x2E05,
    *lr(0x2E06, 0x2E08),
    0x2E09,
    0x2E0A,
    0x2E0B,
    0x2E0C,
    0x2E0D,
    *lr(0x2E0E, 0x2E16),
    0x2E17,
    *lr(0x2E18, 0x2E19),
    0x2E1A,
    0x2E1B,
    0x2E1C,
    0x2E1D,
    *lr(0x2E1E, 0x2E1F),
    0x2E20,
    0x2E21,
    0x2E22,
    0x2E23,
    0x2E24,
    0x2E25,
    0x2E26,
    0x2E27,
    0x2E28,
    0x2E29,
    *lr(0x2E2A, 0x2E2E),
    0x2E2F,
    *lr(0x2E30, 0x2E39),
    *lr(0x2E3A, 0x2E3B),
    *lr(0x2E3C, 0x2E3F),
    0x2E40,
    0x2E41,
    0x2E42,
    *lr(0x2E43, 0x2E4F),
    *lr(0x2E50, 0x2E51),
    *lr(0x2E52, 0x2E54),
    0x2E55,
    0x2E56,
    0x2E57,
    0x2E58,
    0x2E59,
    0x2E5A,
    0x2E5B,
    0x2E5C,
    0x2E5D,
    *lr(0x2FF0, 0x2FFF),
    0x3000,
    *lr(0x3001, 0x3003),
    0x3004,
    0x3006,
    0x3008,
    0x3009,
    0x300A,
    0x300B,
    0x300C,
    0x300D,
    0x300E,
    0x300F,
    0x3010,
    0x3011,
    *lr(0x3012, 0x3013),
    0x3014,
    0x3015,
    0x3016,
    0x3017,
    0x3018,
    0x3019,
    0x301A,
    0x301B,
    0x301C,
    0x301D,
    *lr(0x301E, 0x301F),
    0x3020,
    0x3030,
    *lr(0x3031, 0x3035),
    *lr(0x3036, 0x3037),
    0x303C,
    0x303D,
    *lr(0x303E, 0x303F),
    *lr(0x309B, 0x309C),
    0x30A0,
    0x30FB,
    0x30FC,
    *lr(0x3190, 0x3191),
    *lr(0x3192, 0x3195),
    *lr(0x3196, 0x319F),
    *lr(0x31C0, 0x31E3),
    0x31EF,
    *lr(0x3220, 0x3229),
    *lr(0x322A, 0x3247),
    *lr(0x3248, 0x324F),
    0x3250,
    *lr(0x3251, 0x325F),
    0x327F,
    *lr(0x3280, 0x3289),
    *lr(0x328A, 0x32B0),
    *lr(0x32B1, 0x32BF),
    *lr(0x32C0, 0x32CF),
    0x32FF,
    *lr(0x3358, 0x33FF),
    *lr(0x4DC0, 0x4DFF),
    *lr(0xA700, 0xA716),
    *lr(0xA717, 0xA71F),
    *lr(0xA720, 0xA721),
    0xA788,
    *lr(0xA789, 0xA78A),
    *lr(0xA830, 0xA835),
    *lr(0xA836, 0xA837),
    0xA838,
    0xA839,
    0xA92E,
    0xA9CF,
    0xAB5B,
    *lr(0xAB6A, 0xAB6B),
    0xFD3E,
    0xFD3F,
    *lr(0xFE10, 0xFE16),
    0xFE17,
    0xFE18,
    0xFE19,
    0xFE30,
    *lr(0xFE31, 0xFE32),
    *lr(0xFE33, 0xFE34),
    0xFE35,
    0xFE36,
    0xFE37,
    0xFE38,
    0xFE39,
    0xFE3A,
    0xFE3B,
    0xFE3C,
    0xFE3D,
    0xFE3E,
    0xFE3F,
    0xFE40,
    0xFE41,
    0xFE42,
    0xFE43,
    0xFE44,
    *lr(0xFE45, 0xFE46),
    0xFE47,
    0xFE48,
    *lr(0xFE49, 0xFE4C),
    *lr(0xFE4D, 0xFE4F),
    *lr(0xFE50, 0xFE52),
    *lr(0xFE54, 0xFE57),
    0xFE58,
    0xFE59,
    0xFE5A,
    0xFE5B,
    0xFE5C,
    0xFE5D,
    0xFE5E,
    *lr(0xFE5F, 0xFE61),
    0xFE62,
    0xFE63,
    *lr(0xFE64, 0xFE66),
    0xFE68,
    0xFE69,
    *lr(0xFE6A, 0xFE6B),
    0xFEFF,
    *lr(0xFF01, 0xFF03),
    0xFF04,
    *lr(0xFF05, 0xFF07),
    0xFF08,
    0xFF09,
    0xFF0A,
    0xFF0B,
    0xFF0C,
    0xFF0D,
    *lr(0xFF0E, 0xFF0F),
    *lr(0xFF10, 0xFF19),
    *lr(0xFF1A, 0xFF1B),
    *lr(0xFF1C, 0xFF1E),
    *lr(0xFF1F, 0xFF20),
    0xFF3B,
    0xFF3C,
    0xFF3D,
    0xFF3E,
    0xFF3F,
    0xFF40,
    0xFF5B,
    0xFF5C,
    0xFF5D,
    0xFF5E,
    0xFF5F,
    0xFF60,
    0xFF61,
    0xFF62,
    0xFF63,
    *lr(0xFF64, 0xFF65),
    0xFF70,
    *lr(0xFF9E, 0xFF9F),
    *lr(0xFFE0, 0xFFE1),
    0xFFE2,
    0xFFE3,
    0xFFE4,
    *lr(0xFFE5, 0xFFE6),
    0xFFE8,
    *lr(0xFFE9, 0xFFEC),
    *lr(0xFFED, 0xFFEE),
    *lr(0xFFF9, 0xFFFB),
    *lr(0xFFFC, 0xFFFD),
    *lr(0x10100, 0x10102),
    *lr(0x10107, 0x10133),
    *lr(0x10137, 0x1013F),
    *lr(0x10190, 0x1019C),
    *lr(0x101D0, 0x101FC),
    *lr(0x102E1, 0x102FB),
    *lr(0x1BCA0, 0x1BCA3),
    *lr(0x1CF50, 0x1CFC3),
    *lr(0x1D000, 0x1D0F5),
    *lr(0x1D100, 0x1D126),
    *lr(0x1D129, 0x1D164),
    *lr(0x1D165, 0x1D166),
    *lr(0x1D16A, 0x1D16C),
    *lr(0x1D16D, 0x1D172),
    *lr(0x1D173, 0x1D17A),
    *lr(0x1D183, 0x1D184),
    *lr(0x1D18C, 0x1D1A9),
    *lr(0x1D1AE, 0x1D1EA),
    *lr(0x1D2C0, 0x1D2D3),
    *lr(0x1D2E0, 0x1D2F3),
    *lr(0x1D300, 0x1D356),
    *lr(0x1D360, 0x1D378),
    *lr(0x1D400, 0x1D454),
    *lr(0x1D456, 0x1D49C),
    *lr(0x1D49E, 0x1D49F),
    0x1D4A2,
    *lr(0x1D4A5, 0x1D4A6),
    *lr(0x1D4A9, 0x1D4AC),
    *lr(0x1D4AE, 0x1D4B9),
    0x1D4BB,
    *lr(0x1D4BD, 0x1D4C3),
    *lr(0x1D4C5, 0x1D505),
    *lr(0x1D507, 0x1D50A),
    *lr(0x1D50D, 0x1D514),
    *lr(0x1D516, 0x1D51C),
    *lr(0x1D51E, 0x1D539),
    *lr(0x1D53B, 0x1D53E),
    *lr(0x1D540, 0x1D544),
    0x1D546,
    *lr(0x1D54A, 0x1D550),
    *lr(0x1D552, 0x1D6A5),
    *lr(0x1D6A8, 0x1D6C0),
    0x1D6C1,
    *lr(0x1D6C2, 0x1D6DA),
    0x1D6DB,
    *lr(0x1D6DC, 0x1D6FA),
    0x1D6FB,
    *lr(0x1D6FC, 0x1D714),
    0x1D715,
    *lr(0x1D716, 0x1D734),
    0x1D735,
    *lr(0x1D736, 0x1D74E),
    0x1D74F,
    *lr(0x1D750, 0x1D76E),
    0x1D76F,
    *lr(0x1D770, 0x1D788),
    0x1D789,
    *lr(0x1D78A, 0x1D7A8),
    0x1D7A9,
    *lr(0x1D7AA, 0x1D7C2),
    0x1D7C3,
    *lr(0x1D7C4, 0x1D7CB),
    *lr(0x1D7CE, 0x1D7FF),
    *lr(0x1EC71, 0x1ECAB),
    0x1ECAC,
    *lr(0x1ECAD, 0x1ECAF),
    0x1ECB0,
    *lr(0x1ECB1, 0x1ECB4),
    *lr(0x1ED01, 0x1ED2D),
    0x1ED2E,
    *lr(0x1ED2F, 0x1ED3D),
    *lr(0x1F000, 0x1F02B),
    *lr(0x1F030, 0x1F093),
    *lr(0x1F0A0, 0x1F0AE),
    *lr(0x1F0B1, 0x1F0BF),
    *lr(0x1F0C1, 0x1F0CF),
    *lr(0x1F0D1, 0x1F0F5),
    *lr(0x1F100, 0x1F10C),
    *lr(0x1F10D, 0x1F1AD),
    *lr(0x1F1E6, 0x1F1FF),
    *lr(0x1F201, 0x1F202),
    *lr(0x1F210, 0x1F23B),
    *lr(0x1F240, 0x1F248),
    *lr(0x1F250, 0x1F251),
    *lr(0x1F260, 0x1F265),
    *lr(0x1F300, 0x1F3FA),
    *lr(0x1F3FB, 0x1F3FF),
    *lr(0x1F400, 0x1F6D7),
    *lr(0x1F6DC, 0x1F6EC),
    *lr(0x1F6F0, 0x1F6FC),
    *lr(0x1F700, 0x1F776),
    *lr(0x1F77B, 0x1F7D9),
    *lr(0x1F7E0, 0x1F7EB),
    0x1F7F0,
    *lr(0x1F800, 0x1F80B),
    *lr(0x1F810, 0x1F847),
    *lr(0x1F850, 0x1F859),
    *lr(0x1F860, 0x1F887),
    *lr(0x1F890, 0x1F8AD),
    *lr(0x1F8B0, 0x1F8B1),
    *lr(0x1F900, 0x1FA53),
    *lr(0x1FA60, 0x1FA6D),
    *lr(0x1FA70, 0x1FA7C),
    *lr(0x1FA80, 0x1FA88),
    *lr(0x1FA90, 0x1FABD),
    *lr(0x1FABF, 0x1FAC5),
    *lr(0x1FACE, 0x1FADB),
    *lr(0x1FAE0, 0x1FAE8),
    *lr(0x1FAF0, 0x1FAF8),
    *lr(0x1FB00, 0x1FB92),
    *lr(0x1FB94, 0x1FBCA),
    *lr(0x1FBF0, 0x1FBF9),
    0xE0001,
    *lr(0xE0020, 0xE007F),
]

Latin_list = [
    *lr(0x0041, 0x005A),
    *lr(0x0061, 0x007A),
    0x00AA,
    0x00BA,
    *lr(0x00C0, 0x00D6),
    *lr(0x00D8, 0x00F6),
    *lr(0x00F8, 0x01BA),
    0x01BB,
    *lr(0x01BC, 0x01BF),
    *lr(0x01C0, 0x01C3),
    *lr(0x01C4, 0x0293),
    0x0294,
    *lr(0x0295, 0x02AF),
    *lr(0x02B0, 0x02B8),
    *lr(0x02E0, 0x02E4),
    *lr(0x1D00, 0x1D25),
    *lr(0x1D2C, 0x1D5C),
    *lr(0x1D62, 0x1D65),
    *lr(0x1D6B, 0x1D77),
    *lr(0x1D79, 0x1D9A),
    *lr(0x1D9B, 0x1DBE),
    *lr(0x1E00, 0x1EFF),
    0x2071,
    0x207F,
    *lr(0x2090, 0x209C),
    *lr(0x212A, 0x212B),
    0x2132,
    0x214E,
    *lr(0x2160, 0x2182),
    *lr(0x2183, 0x2184),
    *lr(0x2185, 0x2188),
    *lr(0x2C60, 0x2C7B),
    *lr(0x2C7C, 0x2C7D),
    *lr(0x2C7E, 0x2C7F),
    *lr(0xA722, 0xA76F),
    0xA770,
    *lr(0xA771, 0xA787),
    *lr(0xA78B, 0xA78E),
    0xA78F,
    *lr(0xA790, 0xA7CA),
    *lr(0xA7D0, 0xA7D1),
    0xA7D3,
    *lr(0xA7D5, 0xA7D9),
    *lr(0xA7F2, 0xA7F4),
    *lr(0xA7F5, 0xA7F6),
    0xA7F7,
    *lr(0xA7F8, 0xA7F9),
    0xA7FA,
    *lr(0xA7FB, 0xA7FF),
    *lr(0xAB30, 0xAB5A),
    *lr(0xAB5C, 0xAB5F),
    *lr(0xAB60, 0xAB64),
    *lr(0xAB66, 0xAB68),
    0xAB69,
    *lr(0xFB00, 0xFB06),
    *lr(0xFF21, 0xFF3A),
    *lr(0xFF41, 0xFF5A),
    *lr(0x10780, 0x10785),
    *lr(0x10787, 0x107B0),
    *lr(0x107B2, 0x107BA),
    *lr(0x1DF00, 0x1DF09),
    0x1DF0A,
    *lr(0x1DF0B, 0x1DF1E),
    *lr(0x1DF25, 0x1DF2A),
]

Greek_list = [
    *lr(0x0370, 0x0373),
    0x0375,
    *lr(0x0376, 0x0377),
    0x037A,
    *lr(0x037B, 0x037D),
    0x037F,
    0x0384,
    0x0386,
    *lr(0x0388, 0x038A),
    0x038C,
    *lr(0x038E, 0x03A1),
    *lr(0x03A3, 0x03E1),
    *lr(0x03F0, 0x03F5),
    0x03F6,
    *lr(0x03F7, 0x03FF),
    *lr(0x1D26, 0x1D2A),
    *lr(0x1D5D, 0x1D61),
    *lr(0x1D66, 0x1D6A),
    0x1DBF,
    *lr(0x1F00, 0x1F15),
    *lr(0x1F18, 0x1F1D),
    *lr(0x1F20, 0x1F45),
    *lr(0x1F48, 0x1F4D),
    *lr(0x1F50, 0x1F57),
    0x1F59,
    0x1F5B,
    0x1F5D,
    *lr(0x1F5F, 0x1F7D),
    *lr(0x1F80, 0x1FB4),
    *lr(0x1FB6, 0x1FBC),
    0x1FBD,
    0x1FBE,
    *lr(0x1FBF, 0x1FC1),
    *lr(0x1FC2, 0x1FC4),
    *lr(0x1FC6, 0x1FCC),
    *lr(0x1FCD, 0x1FCF),
    *lr(0x1FD0, 0x1FD3),
    *lr(0x1FD6, 0x1FDB),
    *lr(0x1FDD, 0x1FDF),
    *lr(0x1FE0, 0x1FEC),
    *lr(0x1FED, 0x1FEF),
    *lr(0x1FF2, 0x1FF4),
    *lr(0x1FF6, 0x1FFC),
    *lr(0x1FFD, 0x1FFE),
    0x2126,
    0xAB65,
    *lr(0x10140, 0x10174),
    *lr(0x10175, 0x10178),
    *lr(0x10179, 0x10189),
    *lr(0x1018A, 0x1018B),
    *lr(0x1018C, 0x1018E),
    0x101A0,
    *lr(0x1D200, 0x1D241),
    *lr(0x1D242, 0x1D244),
    0x1D245,
]

Cyrillic_list = [
    *lr(0x0400, 0x0481),
    0x0482,
    *lr(0x0483, 0x0484),
    0x0487,
    *lr(0x0488, 0x0489),
    *lr(0x048A, 0x052F),
    *lr(0x1C80, 0x1C88),
    0x1D2B,
    0x1D78,
    *lr(0x2DE0, 0x2DFF),
    *lr(0xA640, 0xA66D),
    0xA66E,
    0xA66F,
    *lr(0xA670, 0xA672),
    0xA673,
    *lr(0xA674, 0xA67D),
    0xA67E,
    0xA67F,
    *lr(0xA680, 0xA69B),
    *lr(0xA69C, 0xA69D),
    *lr(0xA69E, 0xA69F),
    *lr(0xFE2E, 0xFE2F),
    *lr(0x1E030, 0x1E06D),
    0x1E08F,
]

Hebrew_list = [
    *lr(0x0591, 0x05BD),
    0x05BE,
    0x05BF,
    0x05C0,
    *lr(0x05C1, 0x05C2),
    0x05C3,
    *lr(0x05C4, 0x05C5),
    0x05C6,
    0x05C7,
    *lr(0x05D0, 0x05EA),
    *lr(0x05EF, 0x05F2),
    *lr(0x05F3, 0x05F4),
    0xFB1D,
    0xFB1E,
    *lr(0xFB1F, 0xFB28),
    0xFB29,
    *lr(0xFB2A, 0xFB36),
    *lr(0xFB38, 0xFB3C),
    0xFB3E,
    *lr(0xFB40, 0xFB41),
    *lr(0xFB43, 0xFB44),
    *lr(0xFB46, 0xFB4F),
]

Han_list = [
    *lr(0x2E80, 0x2E99),
    *lr(0x2E9B, 0x2EF3),
    *lr(0x2F00, 0x2FD5),
    0x3005,
    0x3007,
    *lr(0x3021, 0x3029),
    *lr(0x3038, 0x303A),
    0x303B,
    *lr(0x3400, 0x4DBF),
    *lr(0x4E00, 0x9FFF),
    *lr(0xF900, 0xFA6D),
    *lr(0xFA70, 0xFAD9),
    0x16FE2,
    0x16FE3,
    *lr(0x16FF0, 0x16FF1),
    *lr(0x20000, 0x2A6DF),
    *lr(0x2A700, 0x2B739),
    *lr(0x2B740, 0x2B81D),
    *lr(0x2B820, 0x2CEA1),
    *lr(0x2CEB0, 0x2EBE0),
    *lr(0x2EBF0, 0x2EE5D),
    *lr(0x2F800, 0x2FA1D),
    *lr(0x30000, 0x3134A),
    *lr(0x31350, 0x323AF),
]

Katakana_list = [
    *lr(0x30A1, 0x30FA),
    *lr(0x30FD, 0x30FE),
    0x30FF,
    *lr(0x31F0, 0x31FF),
    *lr(0x32D0, 0x32FE),
    *lr(0x3300, 0x3357),
    *lr(0xFF66, 0xFF6F),
    *lr(0xFF71, 0xFF9D),
    *lr(0x1AFF0, 0x1AFF3),
    *lr(0x1AFF5, 0x1AFFB),
    *lr(0x1AFFD, 0x1AFFE),
    0x1B000,
    *lr(0x1B120, 0x1B122),
    0x1B155,
    *lr(0x1B164, 0x1B167),
]

Hiragana_list = [
    *lr(0x3041, 0x3096),
    *lr(0x309D, 0x309E),
    0x309F,
    *lr(0x1B001, 0x1B11F),
    0x1B132,
    *lr(0x1B150, 0x1B152),
    0x1F200,
]

Bopomofo_list = [
    *lr(0x02EA, 0x02EB),
    *lr(0x3105, 0x312F),
    *lr(0x31A0, 0x31BF),
]

Hangul_list = [
    *lr(0x1100, 0x11FF),
    *lr(0x302E, 0x302F),
    *lr(0x3131, 0x318E),
    *lr(0x3200, 0x321E),
    *lr(0x3260, 0x327E),
    *lr(0xA960, 0xA97C),
    *lr(0xAC00, 0xD7A3),
    *lr(0xD7B0, 0xD7C6),
    *lr(0xD7CB, 0xD7FB),
    *lr(0xFFA0, 0xFFBE),
    *lr(0xFFC2, 0xFFC7),
    *lr(0xFFCA, 0xFFCF),
    *lr(0xFFD2, 0xFFD7),
    *lr(0xFFDA, 0xFFDC),
]
