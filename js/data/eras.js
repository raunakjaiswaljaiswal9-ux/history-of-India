/**
 * Historical Eras Dataset - History of India
 * Sourced with high-resolution authentic photography stored in images/ directory.
 */

window.HistoryData = window.HistoryData || {};

window.HistoryData.eras = [
  {
    id: "indus-valley",
    title: "Indus Valley Civilization",
    subtitle: "The Bronze Age Urban Metropolis",
    period: "3300 BCE – 1300 BCE",
    category: "ancient",
    image: "images/priest_king.jpg",
    banner: "images/dancing_girl.jpg",
    capital: "Mohenjo-daro, Harappa, Dholavira, Rakhigarhi",
    geography: "Indus and Ghaggar-Hakra River Basins (Northwest Subcontinent)",
    overview: "Spanning over 1 million square kilometers, the Harappan civilization was an engineering marvel characterized by rectilinear grid city planning, advanced hydraulic sanitation systems, standardized baked brick dimensions, and peaceful maritime commerce with ancient Sumer and Elam.",
    stats: {
      duration: "2,000 Years",
      majorSites: "1,400+ Excavated Sites",
      tradePartners: "Mesopotamia, Oman, Persian Gulf",
      innovation: "Standardized Weights & Measures"
    },
    keyEvents: [
      { year: "c. 3300 BCE", title: "Early Harappan (Ravi Phase)", desc: "Emergence of fortified agricultural villages, early pottery, and preliminary script marks." },
      { year: "c. 2600 BCE", title: "Mature Harappan Zenith", desc: "Construction of multi-story brick homes, the Great Bath at Mohenjo-daro, and tidal dockyards at Lothal." },
      { year: "c. 1900 BCE", title: "Late Harappan De-urbanization", desc: "Monsoonal shifts and river course variations lead to eastward dispersal towards the Gangetic valley." }
    ],
    prominentFigures: ["The Priest-King", "The Dancing Girl Sculptor", "Harappan Maritime Navigators"]
  },
  {
    id: "vedic-age",
    title: "Vedic Era & Mahajanapadas",
    subtitle: "Philosophical Dawn & The 16 Great Republics",
    period: "1500 BCE – 322 BCE",
    category: "ancient",
    image: "images/ashoka_pillar.jpg",
    banner: "images/sanchi_stupa.jpg",
    capital: "Kashi, Kosala, Magadha (Rajagriha), Vaishali",
    geography: "Indo-Gangetic Plain",
    overview: "The foundational era of Indian philosophy, witnessing the compilation of the sacred Vedas, the sublime metaphysics of the Upanishads, the dawn of the Iron Age, and the profound humanitarian philosophies of Gautama Buddha and Lord Mahavira.",
    stats: {
      duration: "1,180 Years",
      keyTexts: "Rigveda, Sama, Yajur, Atharva & 108 Upanishads",
      polities: "16 Mahajanapadas (Monarchies & Republics)",
      thinkers: "Gautama Buddha, Mahavira, Panini"
    },
    keyEvents: [
      { year: "c. 1500 BCE", title: "Composition of Rigvedic Hymns", desc: "Sanskrit oral tradition crystallizes philosophical inquiry into creation and the cosmos." },
      { year: "c. 600 BCE", title: "Rise of the 16 Mahajanapadas", desc: "Formation of powerful urban states like Magadha, Kosala, and the democratic Licchavi republic." },
      { year: "c. 528 BCE", title: "Buddha's Enlightenment at Bodh Gaya", desc: "Siddhartha Gautama attains Nirvana and preaches the Four Noble Truths and Eightfold Path at Sarnath." }
    ],
    prominentFigures: ["Gautama Buddha", "Lord Mahavira", "Panini (Father of Linguistics)", "Bimbisara"]
  },
  {
    id: "classical-mauryas",
    title: "The Maurya Empire",
    subtitle: "Pan-Indian Unity & Ashoka's Edicts of Peace",
    period: "322 BCE – 185 BCE",
    category: "classical",
    image: "images/ashoka_lion.jpg",
    banner: "images/sanchi_stupa.jpg",
    capital: "Pataliputra (Modern Patna)",
    geography: "Entire Subcontinent, spanning Afghanistan to the Deccan",
    overview: "Founded by Chandragupta Maurya under the mentorship of polymath Chanakya (author of Arthashastra), the Maurya Empire unified nearly the entire subcontinent. Emperor Ashoka the Great, following the Kalinga War, established an empire of moral governance, carving pillars of peace that now form India's national emblem.",
    stats: {
      duration: "137 Years",
      peakTerritory: "5,000,000 km² (Largest in Indian History)",
      capitalPopulation: "~400,000 in Pataliputra",
      monuments: "Ashoka Pillars, Rock Edicts, Sanchi Stupa"
    },
    keyEvents: [
      { year: "322 BCE", title: "Founding by Chandragupta Maurya", desc: "Overthrow of the Nanda dynasty and decisive victory against Alexander's general Seleucus I." },
      { year: "261 BCE", title: "The Kalinga War & Transformation", desc: "Ashoka renounces military conquest (Digvijaya) in favor of moral victory (Dhammavijaya)." },
      { year: "250 BCE", title: "Third Buddhist Council", desc: "Convened at Pataliputra; emissaries dispatched across Sri Lanka, Greece, and Southeast Asia." }
    ],
    prominentFigures: ["Chandragupta Maurya", "Chanakya (Kautilya)", "Ashoka the Great", "Megasthenes"]
  },
  {
    id: "golden-age-guptas",
    title: "The Gupta Golden Age",
    subtitle: "Renaissance of Science, Mathematics & Classical Arts",
    period: "320 CE – 550 CE",
    category: "classical",
    image: "images/nalanda_ruins.jpg",
    banner: "images/ajanta_caves.jpg",
    capital: "Pataliputra & Ujjain",
    geography: "Northern, Central, and Eastern Subcontinent",
    overview: "Regarded as the Golden Age of India, this epoch generated revolutionary breakthroughs in mathematics (concept of zero, decimal system, pi calculation), astronomy by Aryabhata, immortal Sanskrit dramaturgy by Kalidasa, and the flourishing of Nalanda University.",
    stats: {
      duration: "230 Years",
      discoveries: "Zero, Decimal Notation, Earth's Axial Rotation",
      institutions: "Nalanda University (10,000 students, 2,000 teachers)",
      artStyle: "Ajanta Cave Paintings, Iron Pillar Metallurgy"
    },
    keyEvents: [
      { year: "375 CE", title: "Reign of Chandragupta II (Vikramaditya)", desc: "A zenith of court culture, patronizing the Nine Gems (Navaratnas) including poet Kalidasa." },
      { year: "499 CE", title: "Aryabhata Authors Aryabhatiya", desc: "Mathematical treatise calculating the solar year to 365.358 days and stating the earth rotates on its axis." },
      { year: "c. 5th Century", title: "Expansion of Nalanda Mahavihara", desc: "Becomes the intellectual hub of Asia, hosting scholars from China, Korea, Tibet, and Persia." }
    ],
    prominentFigures: ["Chandragupta Vikramaditya", "Aryabhata", "Kalidasa", "Varahamihira", "Dhanvantari"]
  },
  {
    id: "medieval-dynasties",
    title: "Cholas & Medieval Grandeur",
    subtitle: "Oceanic Fleets & Monumental Living Temples",
    period: "850 CE – 1526 CE",
    category: "medieval",
    image: "images/brihadisvara.jpg",
    banner: "images/hampi_chariot.jpg",
    capital: "Thanjavur, Gangaikonda Cholapuram, Hampi",
    geography: "Southern India, Deccan, and Bay of Bengal Maritime Sphere",
    overview: "An era of sublime granite architecture, lost-wax bronze artistry, and maritime hegemony. The Imperial Cholas created an oceanic blue-water navy dominating the Strait of Malacca, while the Vijayanagara Empire stood as one of the richest and most cosmopolitan empires of the medieval globe.",
    stats: {
      duration: "676 Years",
      navalReach: "Sumatra, Java, Malaya (Srivijaya Empire)",
      architecture: "Great Living Chola Temples & Hampi Monuments",
      metallurgy: "Chola Nataraja Bronzes (World Masterpieces)"
    },
    keyEvents: [
      { year: "1010 CE", title: "Consecration of Brihadisvara Temple", desc: "Raja Raja Chola I completes the 216-foot granite Vimana topped with an 80-ton single stone dome." },
      { year: "1025 CE", title: "Rajendra Chola's Maritime Expedition", desc: "Naval armadas cross the Indian Ocean to secure trade routes and conquer Southeast Asian ports." },
      { year: "1509 CE", title: "Golden Reign of Krishnadevaraya", desc: "Vijayanagara reaches its cultural peak, patronizing Ashtadiggajas (eight Telugu literary masters)." }
    ],
    prominentFigures: ["Raja Raja Chola I", "Rajendra Chola", "Krishnadevaraya", "Rani Rudrama Devi"]
  },
  {
    id: "mughal-empire",
    title: "The Mughal Empire",
    subtitle: "Indo-Islamic Synthesis & Architectural Wonders",
    period: "1526 CE – 1857 CE",
    category: "medieval",
    image: "images/taj_mahal.jpg",
    banner: "images/red_fort.jpg",
    capital: "Agra, Fatehpur Sikri, Shahjahanabad (Delhi)",
    geography: "Subcontinent from Kabul to the Deccan plateau",
    overview: "A dynasty renowned for lavish courtly culture, administrative centralization, and breathtaking architecture combining Persian, Indian, and Central Asian styles. Under Akbar the Great, policies of universal peace (Sulh-i-kul) fostered religious debate, while Shah Jahan constructed the Taj Mahal.",
    stats: {
      duration: "331 Years",
      globalEconomy: "Estimated 24% of World GDP in 1700 CE",
      monuments: "Taj Mahal, Red Fort, Humayun's Tomb, Fatehpur Sikri",
      arts: "Miniature Painting, Classical Hindustani Music, Urdu Poetry"
    },
    keyEvents: [
      { year: "1526 CE", title: "First Battle of Panipat", desc: "Babur introduces field artillery and tactical cavalry to establish Mughal dominion." },
      { year: "1556–1605 CE", title: "Reign of Akbar the Great", desc: "Abolition of pilgrim taxes, establishment of the Ibadat Khana, and revenue administration under Raja Todar Mal." },
      { year: "1632–1653 CE", title: "Construction of the Taj Mahal", desc: "Shah Jahan commissions the world-renowned white marble mausoleum along the Yamuna river." }
    ],
    prominentFigures: ["Akbar the Great", "Birbal", "Shah Jahan", "Tansen", "Abul Fazl"]
  },
  {
    id: "colonial-struggle",
    title: "The Freedom Struggle",
    subtitle: "From Colonial Bondage to Midnight Sovereignty",
    period: "1757 CE – 1947 CE",
    category: "modern",
    image: "images/gandhi_salt_march.jpg",
    banner: "images/subhas_chandra_bose.jpg",
    capital: "Calcutta (until 1911) / New Delhi",
    geography: "Pan-Indian Territory and International Alliances",
    overview: "Following the Battle of Plassey and the Revolt of 1857, India was subjected to colonial British exploitation. Over nearly a century, diverse movements—from Mahatma Gandhi's Satyagraha to Subhas Chandra Bose's Indian National Army and the sacrifices of Bhagat Singh—culminated in independence on August 15, 1947.",
    stats: {
      duration: "190 Years of British Rule",
      movements: "1857 Revolt, Non-Cooperation, Civil Disobedience, Quit India",
      militaryAction: "Indian National Army (Azad Hind Fauj)",
      historicDate: "August 15, 1947 (Midnight Freedom)"
    },
    keyEvents: [
      { year: "1857", title: "First War of Indian Independence", desc: "Mass revolt across Northern and Central India; end of Company rule and transfer to British Crown." },
      { year: "1930", title: "Dandi Salt March", desc: "Gandhi marches 390 kilometers to break the salt monopoly, captivating global conscience." },
      { year: "1947", title: "Tryst with Destiny", desc: "Jawaharlal Nehru delivers the historic midnight speech as the Indian Tricolor is hoisted at the Red Fort." }
    ],
    prominentFigures: ["Mahatma Gandhi", "Subhas Chandra Bose", "Bhagat Singh", "Sardar Vallabhbhai Patel", "Sarojini Naidu", "Jawaharlal Nehru"]
  },
  {
    id: "modern-republic",
    title: "The Modern Republic",
    subtitle: "Democracy, Space Frontiers & 21st-Century Power",
    period: "1950 CE – Present",
    category: "modern",
    image: "images/constitution_preamble.jpg",
    banner: "images/chandrayaan3.jpg",
    capital: "New Delhi",
    geography: "28 States and 8 Union Territories",
    overview: "Adopting the world's longest written democratic constitution drafted under Dr. B.R. Ambedkar, modern India transformed into the world's largest democracy, an economic engine, and an interplanetary spacefaring nation landing missions on the Moon and Mars.",
    stats: {
      duration: "75+ Years of Republic",
      population: "1.4+ Billion Citizens",
      spaceFeats: "Chandrayaan-3 Moon Landing, Mangalyaan Mars Orbiter",
      democracy: "Largest Electorate in Human History"
    },
    keyEvents: [
      { year: "Jan 26, 1950", title: "Enactment of the Constitution", desc: "India officially becomes a Sovereign, Democratic Republic under President Dr. Rajendra Prasad." },
      { year: "1969", title: "Establishment of ISRO", desc: "Dr. Vikram Sarabhai initiates India's space program, emphasizing self-reliance and satellite communications." },
      { year: "2023", title: "Chandrayaan-3 South Pole Landing", desc: "India becomes the first nation on Earth to touch down on the unexplored lunar south pole." }
    ],
    prominentFigures: ["Dr. B.R. Ambedkar", "Dr. Homi Bhabha", "Dr. Vikram Sarabhai", "Dr. A.P.J. Abdul Kalam"]
  }
];
