#!/usr/bin/env python3
"""Generate full EDMO Pulse Wiki — pages, bundle, and viz."""
import json, os, shutil

HOME = os.path.expanduser("~")
WIKI = f"{HOME}/edmo-pulse-wiki"
OLD_WIKI = f"{HOME}/bilgi-llm-wiki/raw/articles"

ARTICLES = [
    {
        "slug": "2026-03-26-edmo-pulse",
        "date": "March 26, 2026",
        "title": "AI-Generated Content Shaping European Perceptions of Gulf Conflicts",
        "url": "https://edmo.eu/publications/ai-and-more-shaping-gulf-war-perceptions-in-europe/",
        "sections": ["GLOBAL PULSE"],
        "summary": "AI-generated content shaping European perceptions of Gulf conflicts. Foreign influence operations in the Baltics. Disinformation surrounding the Artemis II mission."
    },
    {
        "slug": "2026-04-01-edmo-pulse",
        "date": "April 1, 2026",
        "title": "Hungarian Electoral Campaign Disinformation",
        "url": "https://edmo.eu/publications/a-dystopian-electoral-campaign-will-be-over-soon-in-hungary-but-disinformations-damages-are-here-to-stay/",
        "sections": ["ELECTION BEAT"],
        "summary": "Hungarian electoral campaign disinformation. Lasting damage of disinformation campaigns. Prebunking false flag operations before the Hungarian elections."
    },
    {
        "slug": "2026-04-16-edmo-pulse",
        "date": "April 16, 2026",
        "title": "Orbán Has Been Defeated, But What Comes Next?",
        "url": "https://edmo.eu/publications/orban-has-been-defeated-but-what-comes-next/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Post-Orbán Hungary disinformation landscape. Political ads evade moderation. Gen-AI content and election integrity. Bulgarian electoral disinformation. Drones in the Baltics and Russian propaganda. Chat Control 2.0 and European public opinion."
    },
    {
        "slug": "2026-04-23-edmo-pulse",
        "date": "April 23, 2026",
        "title": "AI Slop: How Greed Is Affecting Democracies",
        "url": "https://edmo.eu/publications/ai-slop-how-greed-is-affecting-democracies/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "AI slop content flooding platforms. Fake AI feel-good stories in Malta. Telegram as Bulgarian elections blindspot. Pope Leo XIV vs Trump false claims. The importance of united and socially aware research."
    },
    {
        "slug": "2026-04-30-edmo-pulse",
        "date": "April 30, 2026",
        "title": "Trump's Assassination Attempts and Related Disinformation Are Two Sides of the Same Coin",
        "url": "https://edmo.eu/publications/trumps-assassination-attempts-and-related-disinformation-are-two-sides-of-the-same-coin/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Disinformation narratives surrounding Trump assassination attempts. Vaccine misinformation in Italy. French election disinformation ecosystem. AI-generated content and electoral integrity. Deepfakes in Turkish politics."
    },
    {
        "slug": "2026-05-07-edmo-pulse",
        "date": "May 7, 2026",
        "title": "From Zelensky to Magyar: Old and New Attempts at Disinformation-Driven Character Assassination",
        "url": "https://edmo.eu/publications/from-zelensky-to-magyar-old-and-new-attempts-at-disinformation-driven-character-assassination/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Disinformation-driven character assassination targeting Zelensky and Magyar. Romanian elections disinformation. UK local elections and AI-generated content. Climate disinformation narratives."
    },
    {
        "slug": "2026-05-14-edmo-pulse",
        "date": "May 14, 2026",
        "title": "Hantavirus-Related Disinformation, a New Menace for Bodies and Minds?",
        "url": "https://edmo.eu/publications/hantavirus-related-disinformation-a-new-menace-for-bodies-and-minds/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Hantavirus disinformation and health misinformation. AI-generated political content in Baltic states. Russian disinformation campaigns. Disinformation narratives around migration and crime."
    },
    {
        "slug": "2026-05-21-edmo-pulse",
        "date": "May 21, 2026",
        "title": "Crime, Migrants and Disinformation: An Online Banquet for Extremists, a Real-World Danger for Societies",
        "url": "https://edmo.eu/publications/crime-migrants-and-disinformation-an-online-banquet-for-extremists-a-real-world-danger-for-societies/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Crime and migration disinformation fueling extremism. Romanian presidential election interference. German AfD AI-generated content. Disinformation about Ukraine war narratives. Platform accountability."
    },
    {
        "slug": "2026-05-29-edmo-pulse",
        "date": "May 29, 2026",
        "title": "AI-Political Influencers: The New Gods of Propaganda and Disinformation?",
        "url": "https://edmo.eu/publications/ai-political-influencers-the-new-gods-of-propaganda-and-disinformation/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "AI-powered political influencers as new propaganda vectors. Spanish local elections disinformation. Deepfake detection advances. Russian information operations in Eastern Europe. Media literacy responses."
    },
    {
        "slug": "2026-06-04-edmo-pulse",
        "date": "June 4, 2026",
        "title": "The Same Old Story – A Heat Wave of Climate Disinformation",
        "url": "https://edmo.eu/publications/the-same-old-story-a-heat-wave-of-climate-disinformation/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Climate disinformation during European heatwave. Chromatic change conspiracy theory. Solar energy misinformation. AI-generated climate content. Election disinformation in multiple EU countries. Fact-checking coordination."
    },
    {
        "slug": "2026-06-11-edmo-pulse",
        "date": "June 11, 2026",
        "title": "Incident or Deliberate Action? Drone Crashes Are Always Good for Spreading Conspiracy Theories and Fearmongering",
        "url": "https://edmo.eu/publications/incident-or-deliberate-action-it-doesnt-matter-drone-crashes-are-always-good-for-spreading-conspiracy-theories-and-fearmongering/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Drone crash conspiracy theories. Disinformation about European defense. Romanian election interference update. Russian narratives about Baltic security. Platform content moderation challenges."
    },
    {
        "slug": "2026-06-18-edmo-pulse",
        "date": "June 18, 2026",
        "title": "Dublin, Southport, Belfast: Who Is Fanning the Flames?",
        "url": "https://edmo.eu/publications/dublin-southport-belfast-who-is-fanning-the-flames/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Disinformation following violent incidents in Ireland and UK. Far-right exploitation of tragedies. French legislative elections disinformation. Anti-immigration narratives. Social media platform accountability."
    },
    {
        "slug": "2026-06-25-edmo-pulse",
        "date": "June 25, 2026",
        "title": "The World Cup of Hypersexualized Fakes?",
        "url": "https://edmo.eu/publications/the-world-cup-of-hypersexualized-fakes/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "AI-generated non-consensual intimate content during World Cup. Deepfake pornography and platform responsibility. Electoral disinformation in multiple EU countries. Russian information operations. Digital services act implementation."
    },
    {
        "slug": "2026-07-03-edmo-pulse",
        "date": "July 3, 2026",
        "title": "Climate Change Denialism, and How to Shoot the Messenger to Ignore the Message",
        "url": "https://edmo.eu/publications/climate-change-denialism-and-how-to-shoot-the-messenger-to-ignore-the-message/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Climate change denialism during European heatwave. Chromatic change conspiracy theory. Solar energy misinformation. Moldovan crypto election interference. Crimea sovereignty disinformation. Grooming gang disinformation in Britain. Google Gemini AI video generator risks."
    },
    {
        "slug": "2026-07-09-edmo-pulse",
        "date": "July 9, 2026",
        "title": "Europe Caught in the Crossfire of NATO-related Disinformation",
        "url": "https://edmo.eu/publications/europe-caught-in-the-crossfire-of-nato-related-disinformation/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "NATO disinformation in the lead-up to the Ankara summit. Ukraine drone attack conspiracy theories. Claims about French mercenaries in Ukraine debunked. German social housing vs Ukraine aid misleading narratives. AI video fake about German electoral law. Romanian coordinated Facebook amplification. Russian deflection on Kyiv Pechory Lavra attack. KGB-Palestinian flag myth debunked. RT returns to X despite EU sanctions."
    },
    {
        "slug": "2026-07-16-edmo-pulse",
        "date": "July 16, 2026",
        "title": "So much the worse for the facts?",
        "url": "https://edmo.eu/publications/so-much-the-worse-for-the-facts/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Disinformation's ability to maintain the appearance of being right even when reality proves otherwise. Russian disinformation fabricates evidence of NATO troops in Ukraine; US disinformation claims EU censors free speech. The FIFA World Cup fuels racist and Islamophobic disinformation with decontextualized old videos. AI funeral images inflate support for Iran's former Supreme Leader. Anti-NATO disinformation surges around Ankara summit. World Cup deepfakes and match-fixing allegations. Wildfire conspiracy theories target renewable energy projects."
    },
    {
        "slug": "2026-07-24-edmo-pulse",
        "date": "July 24, 2026",
        "title": "EDMO defending election integrity via the RRS: True transparency and censorship nonsense",
        "url": "https://edmo.eu/publications/edmo-defending-election-integrity-via-the-rrs-true-transparency-and-censorship-nonsense/",
        "sections": ["ON THE RISE", "ZOOM-IN", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Rapid Response System (RRS) transparency. US disinformation campaign against EU digital regulation. Electoral disinformation in Hungary, Bulgaria, Cyprus, Malta. Russian campaign ahead of German elections. Operation Apostle in Malta. Iran/US bases claims. Ukraine war maps. Heatwave conspiracies. Falklands sovereignty debate. European Parliament welcomes EDMO and Media Literacy Expert Group."
    },
    {
        "slug": "2026-08-27-edmo-pulse",
        "date": "August 27, 2026",
        "title": "Ceuta Crisis: First fuelled, then exploited by disinformation",
        "url": "https://edmo.eu/publications/ceuta-crisis-first-fuelled-then-exploited-by-disinformation/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Ceuta migration crisis fuelled and exploited by disinformation. Maldita.es investigation: Arabic-language disinformation triggered the mass influx of 70,000+ people into the Spanish exclave. Far-right networks, Elon Musk and Russia-linked accounts amplified 'invasion' and 'colony' narratives. Recycled videos spark 'second wave' fears. Asylum myths about Moroccans in Spain. 'Dublinants' transfers to Italy under new AMMR rules. Distorted German migration statistics. Swedish ID-less voting backlash and AI-generated election hoaxes. Matryoshka/Storm-1516 target French presidential candidates. Trump NATO spending and inflation claims debunked. Chat Control extension fact-checked. Falklands sovereignty debate. Declining trust in journalism per Reuters Digital News Report 2026."
    },
    {
        "slug": "2026-09-03-edmo-pulse",
        "date": "September 3, 2026",
        "title": "They're (not) eating the cats, again",
        "url": "https://edmo.eu/publications/theyre-not-eating-the-cats-again/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Anti-migrant pet-eating hoax resurfaces after the Ceuta crisis: 'They're (not) eating the cats, again' examines the viral false claim that migrants abuse animals — a classic dehumanisation strategy with Trump's 2024 Haiti precedent, now targeting Moroccan migrants (previously framed as 'zombies'). AI-generated outrage: Chequeado maps fake migrants, protests and voters spreading transnationally (London AI 'migrant neighbourhoods', a fabricated Muslim mayoral candidate in Germany, Mexico AI images of Venezuelan migrants looting). Fact-checks: Canada church fire caused by lightning, not arson by a Muslim migrant (AFP); UK has not agreed to accommodate '4,000 Moroccans' from Ceuta (The Journal); Danish asylum figures in a Ceuta-triggered border debate. Sweden's September 13 election: Russian 'Operation Overload' impersonating news outlets (Kristersson/Ebba Busch pedophile-ring claims) and local Sweden Democrats voter-fraud posts. Germany's Saxony-Anhalt state election: AfD at ~42%, coordinated operations (Storm-1516, Doppelgänger, Matryoshka) amid Berlin's tougher line on Russia (Russian House closure). EDMO Ireland: platforms ignored ~90% of non-AI disinformation in the 2025 presidential election. Nepal glacier-flood disaster videos. 'Hanover Institute' fake think tank poisoning AI chatbots on Israel/Gaza. Iceland's 'sea barons' and the EU referendum."
    },
    {
        "slug": "2026-09-10-edmo-pulse",
        "date": "September 10, 2026",
        "title": "Rewriting the past, endangering the future",
        "url": "https://edmo.eu/publications/rewriting-the-past-endangering-the-future/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Historical memory as a weapon: Ratko Mladić's death reignites one of the Balkans' most toxic battles, with Serbian politicians, media and public figures celebrating the convicted génocidaire as a hero and denying Srebrenica, amplified by Russian state media — an aggressive paranoid nationalism that pushes Serbia away from the EU and raises the risk of renewed violence. Germany's AfD, fresh from 44% in Saxony-Anhalt, proposes cutting Holocaust and Nazism teaching and abolishing the civic-education agency; a redacted German memory serves both Moscow and Washington, which now root for AfD to dismantle the EU. ZOOM-IN digs into historical revisionism online: Maldita/Facta's 2025 'pop fascism' investigation (Franco, Mussolini and Hitler repackaged as memes, music, AI videos and 'Führer Fridays' on TikTok, X, YouTube, Telegram, normalising fascist imagery among young audiences); Provereno Media's 'Holocaust for Sale' exposé of AI-generated fake Holocaust victims on monetised Facebook pages (Auschwitz-Birkenau Museum calls it 'falsification of history'; EDMO Belux's media-literacy tool 'The illusion of the archive'); Funky Citizens/BROD analysis of 9,000+ Telegram posts from 35 groups in Romania's 2024 presidential campaign (Călin Georgescu's idealised Dacian heritage, praise for Legionary leader Codreanu and dictator Antonescu, Holocaust downplaying); and AfD's romanticised Bismarck-era Imperial Germany nostalgia replacing post-WWII remembrance. ELECTION BEAT: a Swedish technical error misregisters up to 500 early votes, fuelling 'election fraud' rumours and the false claim that Election Authority head Anna Nyqvist is a Social Democrat; a viral hospital-closure list omits a centre-right-closure case; and a false German claim that media suppressed the child-abuse sentence of a former SPD deputy mayor (widely covered by Zeit, Spiegel, WDR), countering AfD's 'public-broadcaster capture' narrative. GLOBAL PULSE: the New York Times did NOT report that Saudi Arabia threatened Israel with 'full-scale war' if Turkey were attacked (MedDMO/Cyprus University of Technology); Brazil's October 4 election pits Lula against Flávio Bolsonaro, with an Argentine network falsely claiming Lula triggered a Moroccan migrant influx (the story rested on 50 migrants helped in Florianópolis); and VoxCheck's fact-check of Putin's post-SCO-summit claims (battlefield advances near Sumy/Donetsk, the Black Sea Grain Initiative, strikes on civilian grain vessels, energy-infrastructure 'retaliation'). ON A DIFFERENT NOTE: a Council of Europe study by Iva Nenadić and Marijana Grbeša argues newsfluencers are ambivalent actors — simultaneously a source of democratic opportunity and democratic vulnerability."
    },
    {
        "slug": "2026-09-17-edmo-pulse",
        "date": "September 17, 2026",
        "title": "Fake doctors, real scams: health disinformation exploits desperation",
        "url": "https://edmo.eu/publications/fake-doctors-real-scams-health-disinformation-exploits-desperation/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Health disinformation as an industry of false hope. EDMO monitoring puts health-related disinformation at 7% of all detected EU disinformation in both July and August, with Covid-19 monitored separately at 2% (July) and 4% (August). ON THE RISE argues that 'disinformation about miraculous cures' is the most despicable subcategory - preying on the desperation of people facing serious illness - and that it now operates as an industrial-scale business: AI-generated fake doctors and experts, fabricated studies, false news, videos and images, monetised through platform schemes and amplified by disinformation influencers for whom the lies simply go viral. It places this among other health narratives (sunscreen-causes-cancer claims, Hantavirus fearmongering, the evergreen 'mammography causes cancer' hoax, Trump-boosted vaccine-autism claims) and blames the consistent inability to protect people from scams and demonstrably false content, while noting that regulating US-based platforms is now politically and economically harder than ever for the EU - though it is the right thing to do and can literally save lives. ZOOM-IN: NORDIS/TjekDet expose a network of more than 1,000 AI-generated 'doctors' on YouTube producing around 100,000 misleading videos in 30 languages (fictional personas such as Sofie Larsen advising older men on prostate problems and sexual health, channels monetised via subscriptions, donations and supplement or book sales, some abusing real hospital brands) and list the warning signs of bogus health experts: no uncertainty, emotional language, personal attacks on critics, cherry-picked evidence. BENEDMO debunks TikTok claims that magnesium treats ADHD - lower average magnesium levels in children with ADHD are an association, not causation, studies are inconsistent and evidence for supplements is weak. CEDMO fact-checks viral claims that the anti-parasitic drug mebendazole is a hidden cancer cure: the 2021 Johns Hopkins patent does not prove efficacy, human trials are lacking, and self-medication risks drug interactions and requires liver and anaemia monitoring. ELECTION BEAT: NORDIS/Kallkritikbyran - political scientists Jan Teorell and John Hogstrom say nothing indicates deliberate voter fraud in Sweden despite viral missing-ballot videos (replenishment delays, voters removing rival ballots; a 2022 study found some 40% of election officials had witnessed ballot-paper sabotage), plus the recurring false claim that Election Authority head Anna Nyqvist is a Social Democrat (she has no role in vote counting); Sweden Democrats in Atvidaberg criticised a polling site for turning away a voter over political clothing. BECID - ahead of Latvia's October 3 parliamentary election, four parties fight over the fractured Russian-speaking vote once unified under the collapsed 'Harmony': 'Harmony Center' rebrands around ex-mayor Usakovs's legacy and accuses splinter rivals of betrayal; 'For Stability!' (2022 winner) now frames Ukraine aid as unwanted foreign entanglement; Stepanenko's 'Sovereign Power', polling around 11.8%, pledges to redirect defence spending and end conscription; the ethnically Latvian LPV under Slesers courts Russian speakers more cautiously over new residency language rules. GADMO - German claims that AfD's drop from 51.2% in ballot-box votes to 24.3% by post in Saxony-Anhalt proves postal-vote manipulation; the figures are accurate but no fraud is evidenced (the same pattern appeared in the 2025 Bundestag election, 25.3% vs 13.2%), researcher Simon Franzmann attributes the gap to voter demographics and AfD's own long-standing advice to vote in person, and a staged video falsely depicted destroyed ballots. GLOBAL PULSE: EDMO IRELAND/FactCheck reviews four claims made by Donald Trump in Ireland - that Ireland 'took' US pharmaceutical companies and is 'fleecing' America, that Irish investment in the US nearly doubled, that the Ukraine war is the primary cause of global fuel shortages, and that the US could afford $5,000 per adult - finding facts mixed with misleading context or largely unsupported. IDMO/Facta - the assassination of Charlie Kirk has spawned conspiracy theories inside MAGA itself, with Candace Owens amplifying allegations about Erika Kirk's succession role, turning Kirk's legacy into an internal information war of false claims, harassment and extremist rhetoric that could reshape the movement. IDMO/Facta - Iran floods social platforms with AI-generated videos (fictional English-speaking female soldiers from near-identical accounts created around the same time) to project military strength and legitimacy, some unlabelled, blurring the line between reality and propaganda. ON A DIFFERENT NOTE: MIT research 'Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task' warns of cognitive debt and the need to consider effects on critical thinking and intellectual independence."
    },
    {
        "slug": "2026-09-25-edmo-pulse",
        "date": "September 25, 2026",
        "title": "Even if it doesn't kill us all, AI can still make a lot of damage to our democracies",
        "url": "https://edmo.eu/publications/even-if-it-doesnt-kill-us-all-ai-can-still-make-a-lot-of-damage-to-our-democracies/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Even if it does not kill us all, AI can still make a lot of damage to our democracies. The AI existential-risk debate moves from science fiction to the mainstream: the 9 September resignation of 27-year-old British AI researcher Jacob Coxon (previously OpenAI, then working on pretraining at Anthropic), who wrote that 'The people building AI earnestly believe that it could kill us all by the end of the decade', and the 12 September agreement by the CEOs of Anthropic (Dario Amodei), OpenAI (Sam Altman) and xAI (Elon Musk) that frontier AI development should be slowed with stronger safeguards and greater coordination. But the present is already deeply troubling: CNN reported on 18 September that an intelligence report almost prompted the US military to board a Chinese ship in the Middle East suspected of carrying nuclear-weapons components to Iran - the cargo was misidentified by an AI chatbot used by the analyst who drafted the report, and the mistake was caught only shortly before the planned operation, per a CNN source coming dangerously close to triggering an armed US-China conflict. The editorial argues human oversight is of the utmost importance because AI cannot be blindly trusted, and that in information integrity it is the constant drip of AI-generated falsehoods (amplified, discussed, made viral and monetised with the help of AI itself) that does the greatest damage - eroding trust in institutions, democracy and science, rewriting the past, spreading hate and panic, and reshaping perceptions around artificial realities that reward extremism and polarisation. A catastrophe is no less damaging simply because it unfolds in slow motion. ZOOM-IN: IBERIFIER/Chequeado on whether AI companies should slow development - Amodei, Altman and Musk support caution, external safety evaluations, common standards and coordination between governments, while Mark Zuckerberg and Palantir's Shyam Sankar oppose slowing progress over competition concerns; Chequeado distinguishes hypothetical future risks from harms already documented, citing the 2026 International AI Safety Report commissioned by the UK AI Security Institute (current systems do not yet have the capabilities to escape human control and cause catastrophic destruction but are developing relevant abilities; documented risks include disinformation, influence operations, fraud, cyberattacks and misuse for biological threats; Anthropic reported AI-generated fake identities used to conduct influence operations and Hugging Face reported an autonomous AI agent carrying out 17,600 actions during a cyberattack). IBERIFIER/Chequeado on AI-generated political personas: 'Lucia Libertaria' and 'Julia Riojana' promote pro-government content in Argentina without clearly disclosing their artificial nature, with similar practices in the US (a fictitious female soldier hosting pro-Trump messages), Poland (AI-generated young women promoting anti-EU and far-right narratives) and Germany (attractive synthetic influencers promoting the AfD); the latest evolution comes from Brazil's 4 October general election, where at least 50 AI-generated TikTok videos portraying fictitious voters - some praising, others criticising Lula and Flavio Bolsonaro - reached 7.4 million views overall, a shift from synthetic influencers to 'synthetic voters' that manufactures the appearance of spontaneous citizen testimony. GADMO/AFP on a supposed 1990s street survey video that is entirely AI-generated (95% probability of synthetic audio, 99% for image, unnatural movements, illegible shop signs, and anachronisms such as petrol at 30 pfennigs per litre though 1990s German prices were substantially higher); traced to an account called 'AI Satire' that originally published it with an AI label on TikTok, Facebook and Instagram, it circulated as genuine historical footage once detached from that context - AI reengineering the past to influence perceptions of the present. ELECTION BEAT: BECID/Re:Baltica on the Belarus-based propaganda channel 'Grani Svobodi' ('Borders of Freedom'), with almost 30,000 YouTube subscribers publishing multiple Russian-language videos daily, which uses defectors from Latvia and Lithuania to spread anti-Baltic and anti-Ukrainian narratives to Russian-speaking audiences (the Baltics 'collapsing' because of support for Ukraine, Russophobia and 'Nazism' accusations, questioning the legitimacy of Latvian elections, promoting closer ties with Russia and Belarus; many regular commentators are former activists, politicians and media figures who fled for Russia or Belarus and became active in pro-Kremlin or Belarusian state media); Re:Baltica also investigated Julija Stepanenko, leader and prime ministerial candidate of Latvia's populist right-wing 'Sovereign Power' (running with the 'Alliance of Young Latvia', focused on traditional family values, Christian-right politics and the Russian-speaking minority), who in mid-September 2026 refused to clarify whether she views Russia as a security threat, advocating 'pure diplomacy', while Latvia's State Security Service (SAB) and anti-corruption bureau (KNAB) investigated large financial gifts from her Russia-based father (no legal barrier to her candidacy was found). GADMO/AFP on AI-generated videos during the Mecklenburg-Vorpommern state election falsely claiming the AfD had been omitted from postal ballots in two constituencies: AFP compared the documents with official sample ballots and found the AfD listed in both, the state returning officer confirmed the ballots were forged, analysis tools indicated a 97-99% probability the audio was AI-generated, and an analyst from the Institute for Strategic Dialogue linked the content to the Russian disinformation campaign Storm-1516 (an account spreading the claim had previously amplified narratives associated with the campaign); similar false claims about missing or destroyed AfD ballots circulated around the 2025 federal election and the September 2026 Saxony-Anhalt state election. NORDIS/Kallkritikbyran's ex-post examination of Sweden's elections: misinformation around voter fraud, electoral interference and AI-generated content, with minor voting irregularities and discarded ballots presented as evidence of deliberate fraud and AI-generated images including a fabricated story showing ballots dumped into a river; conspiracy theories alleged manipulation by 'globalist elites' and portrayed immigrants as used to influence the vote (including an AI-generated Islamophobic picture); while foreign actors amplified misleading content, researchers found no immediate evidence of large-scale coordinated foreign interference or significant impact on voters - much of the misinformation originated domestically, highlighting how existing political narratives, conspiracy theories and readily available AI tools contribute to information disorder. MEDDMO on TikTok removing a network of nine fake 'news' accounts that sought to artificially amplify narratives favourable to Malta's Labour Party during the 2026 general election campaign: the Malta-based accounts targeted local users and engaged in coordinated inauthentic behaviour, presenting themselves as news sources, with 433 followers when removed; TikTok did not identify the operators or establish any connection with the Labour Party, which said the accounts were not among its official channels, and earlier reporting had identified TikTok accounts using AI-generated images and videos to attack political figures while a MEDDMO investigation documented websites created ahead of the election that posed as news or fact-checking outlets and promoted pro-Labour narratives. GLOBAL PULSE: IDMO/Facta on Western influencers living in Dubai who post reassuring videos about life in the UAE despite ongoing Iranian missile and drone attacks linked to the wider Middle East conflict, presenting Dubai as safe and well protected by its air defences (some claiming it is safer than many European cities) while other expatriates leave or seek repatriation; Facta notes the strikingly similar messaging mirroring official government communications, the UAE's heavy restrictions on criticism of the government and limited media freedom, and experts' questions about the long-term sustainability of the air-defence system. BROD/Factual fact-checks a viral claim that Europe will stop receiving Russian gas before the winter of 2026-2027 and therefore face widespread heating shortages: the claim misrepresents earlier comments by Vladimir Putin and ignores the EU's gradual phase-out of Russian gas (long-term pipeline contracts can remain in force until autumn 2027), and although EU gas storage levels are lower than in previous years, authorities see no immediate threat to gas security thanks to diversified suppliers, expanded LNG import capacity and reduced consumption, with higher prices and market volatility the main concern rather than households being left without heating. CEDMO on a network of AI-generated deepfake videos falsely depicting celebrities (Alyson Hannigan, Sarah Jessica Parker, Julia Roberts) attacking Democrats, incorporating fake CNN branding, circulating ahead of the 2026 US midterm elections; the celebrities have publicly rejected the fabricated statements, and researchers attribute the campaign to the Russian influence operation Matryoshka (also known as Operation Overload), previously linked to election-related disinformation in several European countries - an early sign of Russian efforts to influence the US midterms through manipulated videos, impersonated media brands and coordinated amplification. ON A DIFFERENT NOTE: the International AI Safety Report 2026 - 'loss of control' scenarios, in which AI systems operate outside anyone's control with no clear path to regaining it, are not possible with current systems but they are improving in relevant areas such as autonomous operation; since the last Report it has become more common for models to distinguish between test settings and real-world deployment and to find loopholes in evaluations, which could allow dangerous capabilities to go undetected before deployment."
    },
    {
        "slug": "2026-10-01-edmo-pulse",
        "date": "October 1, 2026",
        "title": "War in Ukraine: AI-powered disinformation targets mobilization",
        "url": "https://edmo.eu/publications/war-in-ukraine-ai-powered-disinformation-targets-mobilization/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "War in Ukraine: AI-powered disinformation targets mobilization. Disinformation about the war in Ukraine has been a constant phenomenon since Russia's full-scale invasion in February 2022 and, according to EDMO monitoring, has consistently been the main target of disinformation in the European Union in recent months, alongside migration. Recurrent Russian-driven narratives: the Ukrainian government, military and population are largely pro-Nazi; Ukrainian refugees are violent or parasitic and European countries treat them better than their own citizens; Zelenskyy and his entourage are drug users and corrupt; the war is NATO's fault; and it is the West that is seeking escalation. War propaganda is as old as war and used by both sides, but a significant development over the past two years is the growing use of AI to create short videos - usually 5 to 15 seconds long - that are realistic enough to appear credible even though often not technically deepfakes, depicting precisely what propaganda would like to be true: EDMO had already detected a significant wave in late 2025 tied to the Russian offensive on Pokrovsk, with numerous AI-generated videos spread by pro-Russian accounts showing Ukrainian soldiers surrendering or crying. In September a new wave of pro-Russian AI-generated videos was detected, this time focusing on the mobilization of Ukrainian soldiers to the front - soldiers in handcuffs on buses being forcibly taken away - happening alongside Ukrainian armed-forces successes in the Donbas (the liberation of several towns north of Lyman as part of Operation Vivaldi) and intensifying reports of a possible new mobilisation in Russia. The message can target several audiences (the Russian public, the Ukrainian public and public opinion in European countries allied with Kyiv), and the videos are being recirculated in several European countries with subtitles in different languages; AI-generated videos and images are not the only tools, as the campaign also uses the 'old' technique of taking real videos or images and distorting their meaning with false captions - for instance videos and images of a protest against the cutting down of trees in Kyiv circulated with the false claim that they showed Ukrainian civilians being taken away by soldiers for trying to disrupt a recruitment operation. The most concerning element is the relatively low quality and limited coordination of these operations, which combine generative AI with other techniques: the potential for technical and tactical improvement is enormous, and if this content is already capable of causing harm by being believed by more vulnerable segments of the public, thinking about what it could do in the future is chilling. ZOOM-IN (the war increasingly fought in the digital information space, where AI-enabled tools amplify deceptive narratives, manipulate images and facilitate targeted recruitment): NORDIS/TjekDet citing an NGO Code for Africa report exposed 33 recruitment groups running nearly 300 websites and social-media accounts that use deceptive ads - mainly on Facebook and often featuring AI-generated images - to recruit young men from Africa, the Middle East, Asia and Latin America for Russia's war in Ukraine, promising lucrative jobs as security guards, actors or drivers in Russia with monthly salaries exceeding $3,000; upon arrival the men are pressured into signing Russian-language military contracts and sent to the frontlines, many face confiscated passports, threats or unpaid bonuses, and one in five identified African recruits has been killed; experts from the Danish Institute for International Studies note the foreign-recruitment surge offsets domestic soldier shortages while shielding Russia's middle class from mobilization. Ironically the campaigns rely heavily on Western infrastructure: the recruitment group 'IRC Russian Bear' hosts and distributes its campaign materials from a server physically located in Amsterdam; multiple recruitment landing pages and persuasive campaign graphics are built with AI generation tools from US and Swedish companies; and applicant data (private contact details, background profiles and passport information) is collected using software owned by an Austrian tech company before being forwarded to operators in Russia. FACT debunks claims that Kyiv is experiencing a mass exodus as Russia bombards the city: social-media posts circulated photos and videos allegedly showing residents fleeing, but fact-checkers found much of the material misleading or unrelated - one video showed ordinary rush-hour activity in a Kyiv metro station, an image supposedly depicting a traffic jam leaving Kyiv was actually taken at a toll station in China, another photograph showed Ukrainians moving toward the Polish border in 2022 rather than residents fleeing Kyiv in 2026, and a genuine video of Kyiv traffic was misrepresented as evidence of people escaping; analysts say such narratives exaggerate real hardships to create panic, undermine morale and potentially weaken international support for Ukraine, and there is no public evidence of a current mass departure. FACT on AI-generated assessments used to amplify a false claim that a maritime drone destroyed near Romania's Neptun Deep gas platform was 'undoubtedly' Ukrainian: several Romanian media outlets, Facebook pages and Telegram channels cited supposed analyses by ChatGPT, Gemini and Grok as authoritative evidence (one article received over 1,000 reactions, 240 comments and 300 shares, another more than 3,000 reactions, 700 comments and 800 shares), but Fact Hub's experiment found that when given identical photographs and neutral questions the three models produced substantially different identifications, ranging from a possible British-derived vessel to a likely Russian-origin drone and a Ukrainian MAGURA V5, demonstrating how AI outputs can acquire credibility and resonance on social media despite uncertainty, contradictory evidence and the models' own acknowledged limitations. ELECTION BEAT: NORDIS/Kallkritikbyran on Sweden's election aftermath - misinformation around voter fraud, electoral interference and AI-generated content, with minor voting irregularities and discarded ballots often presented as evidence of deliberate fraud and AI-generated images including a fabricated story showing ballots dumped into a river; researchers also identified conspiracy theories alleging manipulation by 'globalist elites' and portraying immigrants as being used to influence the vote (such as an AI-generated Islamophobic picture), narratives that continued circulating after election day; while foreign actors were active in amplifying misleading content, researchers found no immediate evidence of large-scale coordinated foreign interference or significant impact on voters, with much of the misinformation appearing to originate domestically - highlighting how existing political narratives, conspiracy theories and readily available AI tools can contribute to information disorder around elections. GADMO/AFP on postal voting as a target of a disinformation campaign in Berlin and Mecklenburg-Vorpommern: a staged video circulated during Berlin's September 2026 parliamentary election falsely claiming to show postal ballots for the AfD being deliberately destroyed while CDU votes were preserved, fuelling accusations of election fraud, but AFP found the envelopes and documents shown differed from official Berlin postal voting materials and the Berlin state election authority confirmed the video was fake, highlighting inconsistencies with official vote-counting procedures; the video was part of a wider pattern of false claims about postal voting during German state elections in autumn 2026, with similar content in Mecklenburg-Vorpommern and Saxony-Anhalt, some posts attracting unusually high numbers of views compared with their engagement (suggesting possible artificial amplification), and several accounts spreading the claims linked to pro-Russian disinformation networks previously associated with campaigns targeting European elections and promoting narratives favourable to Russia and the AfD. EDMO on Serbia: President Aleksandar Vucic announced extraordinary parliamentary elections for 25 October 2026 despite previously linking the timing of an early vote to the international security situation - in April, amid calls from protesting students for early elections, he said there would be no summer vote if a major global crisis persisted, suggesting elections could instead take place if progress towards peace was made; over the following months he continued to warn about the economic and security consequences of the wars in Ukraine and the Middle East, and in early September expressed concern about growing international tensions and potential wider conflicts while predicting the situation would worsen during the winter; nevertheless on 9 September, following a proposal from the Serbian government, he dissolved parliament and called an early election, and Serbian fact-checking outlet Istinomer assessed his position as inconsistent with his earlier statements. GLOBAL PULSE: CEDMO/Demagog.pl on who creates climate disinformation - it emerges from the intersection of business interests, political actors, propaganda and influence operations, and contemporary climate disinformation rarely denies climate change outright but more often presents climate policies as ineffective, unrealistic, unfair or economically damaging; the article identifies fossil-fuel interests, political actors, think tanks, media, influencers, bots and trolls as participants, and highlights documented historical cases involving Exxon and Shell, whose internal documents acknowledged climate risks while public communications emphasised scientific uncertainty. It also examines Russia's role, arguing climate-related narratives can serve Moscow's economic and geopolitical interests by weakening support for decarbonisation and exploiting divisions over energy prices, renewables and EU policies; many narratives arise locally with local economic or political roots and Russia often does not need to invent conflicts but simply seeks out existing tensions and amplifies them on social media, as seen after the tragic flooding in Valencia when Russian messages reinforced existing criticism of the Spanish authorities and linked the country's weakness to support for Ukraine. DE FACTO/Les Surligneurs examines claims that solar panels significantly increase temperatures and therefore undermine their climate benefits, finding that photovoltaic installations can indeed alter local temperatures but the effect varies considerably by location, weather, panel efficiency and what surfaces they replace: studies recorded increases of up to 5.2 degrees C near rooftop panels during extreme heat, while other research found nighttime warming of 3-4 degrees C above ground-based solar farms; conversely panels can sometimes reduce temperatures, particularly when replacing heat-absorbing surfaces such as asphalt. The article stresses that these localized effects should not be confused with global climate impact - over their life cycle solar panels produce substantially fewer greenhouse-gas emissions than fossil-fuel electricity, and the available evidence indicates photovoltaic energy has a considerably lower carbon footprint than fossil fuels. GADMO on a social-media graphic claiming Germany gives China 630 million euros in annual development aid while China builds hundreds of coal-fired power plants and plans hundreds more: the claim is misleading because it combines outdated figures with current political debates - the figure dates from 2017 and referred largely to repayable loans, not conventional development aid, and Germany has since ended its classic bilateral development cooperation with China, with current German-funded projects much smaller (around 19 million euros committed to environmental and social initiatives, not paid directly to the Chinese government); the figures of about 368 coal plants under construction and 803 planned are also around a decade old, although China continues to expand coal power (94.5 GW of new coal projects began construction in 2024) while rapidly expanding solar energy, which by July 2026 had slightly exceeded coal in installed capacity. ON A DIFFERENT NOTE: the International Panel on the Information Environment's 'Trends in the Information Environment: 2026 Expert Survey Results' - lack of platform accountability was the most widely shared concern, rated a big or extreme threat by 78% of experts, narrowly ahead of misinformation at 73% and polarization at 69%, followed by the dominance of a few social media platforms at 64% and filter bubbles or echo chambers at 53%; generative AI was rated the smallest of the six threats, though still a big or extreme threat for 47% of experts. On barriers, availability of research funding was the most common at 67%, ahead of data access at 60% (funding overtook data access as the top barrier in 2025 and remained the top barrier this year), while pressure to align research with a government's agenda rose from 21% to 33%, government censorship from 11% to 23%, and pressure from private companies from 8% to 18%."
    }
]

def make_page(a):
    tags_list = ["edmo", "weekly-pulse", "disinformation", "europe"]
    if "climate" in a["title"].lower() or "climate" in a["summary"].lower():
        tags_list.append("climate-change")
    if "ai" in a["title"].lower() or "ai" in a["summary"].lower() or "artificial" in a["title"].lower():
        tags_list.append("artificial-intelligence")
    if "elect" in a["title"].lower() or "elect" in a["summary"].lower():
        tags_list.append("elections")
    if "migrat" in a["summary"].lower() or "crime" in a["summary"].lower():
        tags_list.append("migration")
    if "health" in a["title"].lower() or "health" in a["summary"].lower():
        tags_list.append("health-disinformation")
    if "history" in a["title"].lower() or "historical" in a["summary"].lower() or "holocaust" in a["summary"].lower() or "nationalis" in a["summary"].lower():
        tags_list.append("historical-revisionism")
    
    tags_str = "\n".join(f"  - {t}" for t in sorted(set(tags_list)))
    sections_str = "\n".join(f"  - \"{s.upper()}\"" for s in a["sections"])
    
    return f"""---
title: "EDMO Weekly Pulse — {a['date']}"
source: "EDMO"
url: "{a['url']}"
date: "{a['date']}"
type: "weekly-pulse-issue"
sections:
{sections_str}
tags:
{tags_str}
---

## {a['title']}

**{a['date']}** — EDMO Weekly Pulse

{fix_content(a['summary'])}

## Sections

{chr(10).join(f"### {s}" for s in a['sections'])}

### Full Edition

➡️ [Read the full edition on EDMO]({a['url']})

---

*Source: [EDMO Weekly Pulse Archive](https://edmo.eu/pulse/)*

---

## 🔗 Related
- [[entities/edmo.md|European Digital Media Observatory (EDMO)]]
"""

def fix_content(t):
    return t

print("📝 Generating wiki pages...")
os.makedirs(f"{WIKI}/raw", exist_ok=True)
os.makedirs(f"{WIKI}/entities", exist_ok=True)

for a in ARTICLES:
    path = f"{WIKI}/raw/{a['slug']}.md"
    if os.path.exists(path):
        print(f"  ⏭️ {a['slug']}.md (exists, skipped)")
        continue
    with open(path, 'w') as f:
        f.write(make_page(a))
    print(f"  ✅ {a['slug']}.md")

# Entity page
print("\n📝 Generating entity pages...")
entity_md = f"""---
title: "European Digital Media Observatory (EDMO)"
created: 2026-04-16
updated: 2026-09-17
type: entity
tags:
  - institution
  - eu
  - disinformation
  - fact-checking
  - media-literacy
sources:
{chr(10).join(f'  - raw/{a["slug"]}.md' for a in ARTICLES)}
---

# European Digital Media Observatory (EDMO)

AB'nin en büyük disiplinlerarası dezenformasyonla mücadele ağı. **European University Institute** (EUI) Florence School of Transnational Governance bünyesinde faaliyet gösteriyor.

**Kapsam:** 28 AB/AEA ülkesinde 15 ulusal/çokuluslu EDMO hub'ını koordine ediyor.

**Faaliyet Alanları:**
- **Fact-checking:** Dezenformasyon tespiti ve ifşası
- **Media Literacy:** Medya okuryazarlığı eğitimleri ve kaynakları
- **Research:** Dezenformasyon ekosistemi analizi
- **Policy Analysis:** AB dezenformasyon politikalarına katkı

**Hub'lar:** ADMO, BECID, BENEDMO, BROD, CEDMO, DE FACTO, EDMO BELUX, EDMO IRELAND, FACT, GADMO, HDMO, IBERIFIER, IDMO, MEDDMO, NORDIS

**Yayınlar:**
- **Weekly Pulse** — Haftalık dezenformasyon trendleri ve analiz bülteni
- Signals & Noise — Aylık dezenformasyon bülteni
- Best of Fact-checking Map
- EDMO Taskforce Reports

## Weekly Pulse Editions

{chr(10).join(f'- [[raw/{a["slug"]}.md|{a["date"]} — {a["title"]}]]' for a in ARTICLES)}
"""

with open(f"{WIKI}/entities/edmo.md", 'w') as f:
    f.write(entity_md)
print("  ✅ entities/edmo.md")

# Index page
print("\n📝 Generating index page...")
index_md = f"""---
title: "EDMO Weekly Pulse Wiki"
created: 2026-07-08
updated: 2026-09-17
type: index
---

# 📡 EDMO Weekly Pulse Wiki

EDMO (European Digital Media Observatory) tarafından her Perşembe yayınlanan **Weekly Pulse** bülteninin arşiv ve görselleştirme wiki'si.

## Nedir?

Weekly Pulse, Avrupa dezenformasyon ortamındaki güncel trendleri, vakaları ve analizleri derleyen haftalık bir bültendir. EDMO'nun 30 Avrupa ülkesindeki 15 hub'ının çalışmalarını sentezler.

## Bölümler

- **ON THE RISE** — Haftalık yükselen dezenformasyon riskleri
- **ZOOM-IN** — EDMO ağı tarafından tespit edilen vakalar
- **ELECTION BEAT** — Seçim dezenformasyonu takibi
- **GLOBAL PULSE** — Küresel dezenformasyon anlatıları
- **ON A DIFFERENT NOTE** — İlgili konularda kısa analizler

## Tüm Sayılar ({len(ARTICLES)})

| Tarih | Başlık |
|---|---|
{chr(10).join(f'| {a["date"]} | [[raw/{a["slug"]}.md|{a["title"]}]] |' for a in ARTICLES)}

## Künye

- **Yayıncı:** [[entities/edmo.md|European Digital Media Observatory (EDMO)]]
- **Sıklık:** Haftalık (her Perşembe)
- **Arşiv:** [EDMO Pulse](https://edmo.eu/pulse/)
- **Wiki güncelleme:** Otomatik (cronjob ile haftalık)
"""

with open(f"{WIKI}/index.md", 'w') as f:
    f.write(index_md)
print("  ✅ index.md")

# Bundle generation
print("\n📊 Generating bundle.json...")
nodes = []
edges = []
seen_ids = set()

# EDMO entity node
nodes.append({
    "data": {
        "id": "edmo",
        "label": "EDMO",
        "type": "entity",
        "color": "#3b82f6",
        "description": "European Digital Media Observatory",
        "degree": len(ARTICLES) + 5
    }
})
seen_ids.add("edmo")

# Concepts
concepts = [
    ("disinformation", "Dezenformasyon", "#ef4444"),
    ("elections", "Seçim Dezenformasyonu", "#f59e0b"),
    ("ai-content", "AI Üretimi İçerik", "#8b5cf6"),
    ("climate-disinfo", "İklim Dezenformasyonu", "#10b981"),
    ("migration", "Göç ve Suç Anlatıları", "#f97316"),
    ("platform-governance", "Platform Yönetişimi", "#06b6d4"),
    ("deepfakes", "Deepfake", "#ec4899"),
    ("media-literacy", "Medya Okuryazarlığı", "#14b8a6"),
    ("historical-revisionism", "Tarihsel Revizyonizm", "#a855f7"),
    ("health-disinfo", "Sağlık Dezenformasyonu", "#0ea5e9"),
]

for cid, clabel, ccolor in concepts:
    nodes.append({
        "data": {
            "id": cid,
            "label": clabel,
            "type": "concept",
            "color": ccolor,
            "degree": 0,
            "description": f"Kavram: {clabel}"
        }
    })
    seen_ids.add(cid)
    edges.append({
        "data": {
            "id": f"edmo-{cid}",
            "source": "edmo",
            "target": cid,
            "label": "covers"
        }
    })

# Month groups as concept nodes
months_order = [
    ("mar-2026", "March 2026", "#64748b"),
    ("apr-2026", "April 2026", "#64748b"),
    ("may-2026", "May 2026", "#64748b"),
    ("jun-2026", "June 2026", "#64748b"),
    ("jul-2026", "July 2026", "#64748b"),
    ("aug-2026", "August 2026", "#64748b"),
    ("sep-2026", "September 2026", "#64748b"),
    ("oct-2026", "October 2026", "#64748b"),
]
for mid, mlabel, mcolor in months_order:
    nodes.append({
        "data": {
            "id": mid,
            "label": mlabel,
            "type": "concept",
            "color": mcolor,
            "degree": 0,
        }
    })
    seen_ids.add(mid)

# Article nodes
article_tags_map = {
    "2026-03-26-edmo-pulse": ["disinformation", "ai-content"],
    "2026-04-01-edmo-pulse": ["elections", "disinformation"],
    "2026-04-16-edmo-pulse": ["elections", "disinformation"],
    "2026-04-23-edmo-pulse": ["ai-content", "disinformation", "platform-governance"],
    "2026-04-30-edmo-pulse": ["disinformation", "elections", "deepfakes"],
    "2026-05-07-edmo-pulse": ["disinformation", "elections", "ai-content"],
    "2026-05-14-edmo-pulse": ["disinformation", "climate-disinfo"],
    "2026-05-21-edmo-pulse": ["migration", "disinformation", "elections"],
    "2026-05-29-edmo-pulse": ["ai-content", "disinformation", "media-literacy"],
    "2026-06-04-edmo-pulse": ["climate-disinfo", "disinformation", "elections"],
    "2026-06-11-edmo-pulse": ["disinformation", "platform-governance"],
    "2026-06-18-edmo-pulse": ["migration", "disinformation", "platform-governance"],
    "2026-06-25-edmo-pulse": ["deepfakes", "ai-content", "platform-governance"],
    "2026-07-03-edmo-pulse": ["climate-disinfo", "disinformation", "elections", "ai-content"],
    "2026-07-09-edmo-pulse": ["disinformation", "elections", "ai-content", "platform-governance"],
    "2026-07-16-edmo-pulse": ["disinformation", "ai-content", "platform-governance", "climate-disinfo"],
    "2026-07-24-edmo-pulse": ["disinformation", "elections", "platform-governance"],
    "2026-08-27-edmo-pulse": ["migration", "disinformation", "elections"],
    "2026-09-03-edmo-pulse": ["migration", "disinformation", "ai-content", "elections"],
    "2026-09-10-edmo-pulse": ["historical-revisionism", "disinformation", "elections", "ai-content", "media-literacy"],
    "2026-09-17-edmo-pulse": ["health-disinfo", "disinformation", "ai-content", "elections", "platform-governance"],
    "2026-09-25-edmo-pulse": ["ai-content", "disinformation", "elections", "deepfakes", "platform-governance"],
    "2026-10-01-edmo-pulse": ["ai-content", "disinformation", "elections", "climate-disinfo"],
}

month_of = {
    "2026-03": "mar-2026", "2026-04": "apr-2026", "2026-05": "may-2026",
    "2026-06": "jun-2026", "2026-07": "jul-2026", "2026-08": "aug-2026", "2026-09": "sep-2026",
    "2026-10": "oct-2026",
}

for a in ARTICLES:
    month_key = "-".join(a["slug"].split("-")[:2])
    month_node = month_of.get(month_key, "mar-2026")
    
    # Get tag count for sizing
    tags = article_tags_map.get(a["slug"], ["disinformation"])
    degree = len(tags) + 2  # +1 for edmo, +1 for month
    
    nid = a["slug"]
    nodes.append({
        "data": {
            "id": nid,
            "label": a["date"].replace(",", ""),
            "type": "raw_article",
            "color": "#10b981",
            "full_title": a["title"][:60],
            "description": a["summary"][:200],
            "url": a["url"],
            "degree": degree
        }
    })
    seen_ids.add(nid)
    
    # Edge to entity
    edges.append({
        "data": {
            "id": f"edmo-{nid}",
            "source": "edmo",
            "target": nid,
            "label": "published"
        }
    })
    
    # Edge to month
    edges.append({
        "data": {
            "id": f"{nid}-{month_node}",
            "source": nid,
            "target": month_node,
            "label": "in"
        }
    })
    
    # Edges to concepts
    for tag in tags:
        if tag in [c[0] for c in concepts]:
            eid = f"{nid}-{tag}"
            edges.append({
                "data": {
                    "id": eid,
                    "source": nid,
                    "target": tag,
                    "label": "about"
                }
            })

# Sequence edges between consecutive issues
for i in range(len(ARTICLES) - 1):
    edges.append({
        "data": {
            "id": f"{ARTICLES[i]['slug']}-next-{ARTICLES[i+1]['slug']}",
            "source": ARTICLES[i]["slug"],
            "target": ARTICLES[i+1]["slug"],
            "label": "next",
            "color": "#fbbf24"
        }
    })

# Update degrees
degree_map = {}
for e in edges:
    src = e["data"]["source"]
    tgt = e["data"]["target"]
    degree_map[src] = degree_map.get(src, 0) + 1
    degree_map[tgt] = degree_map.get(tgt, 0) + 1

for n in nodes:
    nid = n["data"]["id"]
    if nid in degree_map:
        n["data"]["degree"] = degree_map[nid]

bundle = {"nodes": nodes, "edges": edges}
with open(f"{WIKI}/bundle.json", 'w') as f:
    json.dump(bundle, f, indent=2)
print(f"  ✅ bundle.json ({len(nodes)} nodes, {len(edges)} edges)")

# viz.html
print("📊 Generating viz.html...")
viz_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>EDMO Weekly Pulse — Wiki Viewer</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<script src="https://cdn.jsdelivr.net/npm/cytoscape@3.28.1/dist/cytoscape.min.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;overflow:hidden;background:#0f172a;color:#e2e8f0;height:100vh;display:flex;flex-direction:column}
.hdr{background:linear-gradient(135deg,#1a1a2e,#16213e);padding:10px 20px;display:flex;align-items:center;gap:12px;border-bottom:1px solid #1e293b;flex-shrink:0;flex-wrap:wrap}
.hdr h1{font-size:16px;font-weight:600}
.hdr .sub{font-size:12px;color:#64748b}
.ctrls{display:flex;gap:6px;flex-wrap:wrap;margin-left:auto}
.ctrls button{padding:3px 10px;border-radius:4px;border:1px solid #334155;background:#1e293b;color:#94a3b8;font-size:11px;cursor:pointer}
.ctrls button:hover{background:#334155;color:#e2e8f0}
.ctrls button.on{background:#3b82f6;color:#fff;border-color:#3b82f6}
#cy{flex:1;width:100%;min-height:0}
#info{position:fixed;right:20px;top:60px;width:380px;max-height:80vh;background:#1e293b;border:1px solid #334155;border-radius:8px;padding:16px;overflow-y:auto;display:none;z-index:100;font-size:13px;box-shadow:0 4px 20px rgba(0,0,0,.4)}
#info h2{font-size:14px;margin-bottom:8px;color:#e2e8f0;word-break:break-word}
#info .tp{font-size:11px;color:#64748b;margin-bottom:4px;text-transform:uppercase;letter-spacing:.5px}
#info .desc{color:#94a3b8;margin:8px 0;line-height:1.5;font-size:12px}
#info a{color:#60a5fa}
#info .tags span{display:inline-block;padding:1px 6px;border-radius:3px;background:#334155;color:#94a3b8;font-size:10px;margin:2px}
#info .close{float:right;cursor:pointer;color:#64748b;font-size:18px;line-height:1}
.legend{position:fixed;left:20px;bottom:20px;background:#1e293b;border:1px solid #334155;border-radius:6px;padding:8px 12px;font-size:11px;z-index:50}
.legend .r{display:flex;align-items:center;gap:6px;padding:2px 0}
.legend .d{width:10px;height:10px;border-radius:50%;flex-shrink:0}
#hint{position:fixed;left:50%;top:50%;transform:translate(-50%,-50%);color:#334155;font-size:14px;pointer-events:none;z-index:1;text-align:center;transition:opacity 1s}
@media(max-width:600px){.hdr h1{font-size:14px}.ctrls button{font-size:10px;padding:2px 6px}#info{width:calc(100vw-20px);right:10px;top:50px}}
</style>
</head>
<body>
<div class="hdr">
  <h1>📡 EDMO Weekly Pulse</h1>
  <span class="sub" id="stats">""" + f"{len(nodes)} nodes · {len(edges)} edges" + """</span>
  <div class="ctrls">
    <button onclick="filter('all')" class="on">All</button>
    <button onclick="filter('concept')">🧠 Concept</button>
    <button onclick="filter('entity')">🏛 Entity</button>
    <button onclick="filter('raw_article')">📄 Issues</button>
    <button onclick="layout('cose')">Auto</button>
    <button onclick="layout('grid')">Grid</button>
    <button onclick="layout('breadthfirst')">Timeline</button>
  </div>
</div>
<div id="cy"></div>
<div id="hint">🔍 Zoom &amp; drag to explore…</div>
<div id="info"><span class="close" onclick="closeInfo()">✕</span><div id="info-content"></div></div>
<div class="legend" id="legend"></div>
<script>
var DATA = null;
var cy = null;

function init() {
  fetch('bundle.json')
    .then(function(r) { return r.json(); })
    .then(function(data) {
      DATA = data;
      buildGraph();
      buildLegend();
    })
    .catch(function(err) {
      document.getElementById('stats').textContent = 'Error: ' + err.message;
    });
}

function buildGraph() {
  cy = cytoscape({
    container: document.getElementById('cy'),
    elements: [].concat(DATA.nodes, DATA.edges),
    style: [
      { selector: 'node', style: { 'background-color': 'data(color)', 'label': 'data(label)', 'color': '#f1f5f9', 'font-size': '8px', 'text-valign': 'center', 'text-halign': 'center', 'text-outline-width': 2, 'text-outline-color': '#0f172a', 'width': 'mapData(degree,0,30,20,60)', 'height': 'mapData(degree,0,30,20,60)', 'border-width': 1.5, 'border-color': 'data(color)', 'border-opacity': 0.6, 'background-opacity': 0.85 } },
      { selector: 'node[type="concept"]', style: { 'shape': 'diamond', 'font-weight': 'bold', 'font-size': '9px' } },
      { selector: 'node[type="entity"]', style: { 'shape': 'hexagon', 'font-size': '11px', 'width': 70, 'height': 70 } },
      { selector: 'node[type="raw_article"]', style: { 'shape': 'ellipse', 'font-size': '7px' } },
      { selector: 'edge', style: { 'width': 1, 'line-color': '#334155', 'target-arrow-color': '#334155', 'target-arrow-shape': 'triangle', 'curve-style': 'haystack', 'arrow-scale': 0.5, 'opacity': 0.3 } },
      { selector: 'edge[label="next"]', style: { 'width': 2, 'line-color': '#fbbf24', 'opacity': 0.6, 'curve-style': 'unbundled-bezier', 'target-arrow-shape': 'none' } },
      { selector: ':selected', style: { 'border-width': 3, 'border-color': '#fbbf24', 'border-opacity': 1 } }
    ],
    layout: { name: 'cose', fit: true, padding: 50, nodeRepulsion: 8000, idealEdgeLength: 100, gravity: 0.5 },
    wheelSensitivity: 0.4
  });

  cy.nodes().on('tap', function(e) {
    var node = e.target;
    if (!node.isNode || !node.isNode()) return;
    showInfo(node.data());
  });

  document.getElementById('hint').style.opacity = '0';
  setTimeout(function() { document.getElementById('hint').style.display = 'none'; }, 2000);
  updateStats();
}

function showInfo(d) {
  var el = document.getElementById('info-content');
  var tags = (d.type === 'raw_article') ? '<div class="tags"><span>#' + d.type + '</span></div>' : '';
  var desc = d.description ? '<div class="desc">' + d.description + '</div>' : '';
  var link = d.url ? '<a href="' + d.url + '" target="_blank">🔗 Read full edition →</a>' : '';
  el.innerHTML = '<span class="tp">' + (d.type || 'node') + '</span><h2>' + (d.full_title || d.label || '') + '</h2>' + desc + tags + link;
  document.getElementById('info').style.display = 'block';
}

function closeInfo() { document.getElementById('info').style.display = 'none'; }

function filter(type) {
  var btns = document.querySelectorAll('.ctrls button');
  btns.forEach(function(b) { b.classList.remove('on'); });
  event.target.classList.add('on');
  if (!cy) return;
  if (type === 'all') {
    cy.nodes().show();
    cy.edges().show();
  } else {
    cy.nodes().forEach(function(n) {
      if (n.data('type') === type) n.show();
      else n.hide();
    });
    cy.edges().forEach(function(e) {
      var src = e.source();
      var tgt = e.target();
      if (src.visible() && tgt.visible()) e.show();
      else e.hide();
    });
  }
  updateStats();
}

function layout(name) {
  if (!cy) return;
  var opts = { fit: true, padding: 50, animate: true, duration: 500 };
  if (name === 'grid') opts.name = 'grid';
  else if (name === 'breadthfirst') { opts.name = 'breadthfirst'; opts.roots = '#edmo'; }
  else { opts.name = 'cose'; opts.nodeRepulsion = 8000; opts.idealEdgeLength = 100; opts.gravity = 0.5; }
  cy.layout(opts);
}

function buildLegend() {
  var items = [
    { color: '#3b82f6', label: 'Entity (EDMO)' },
    { color: '#10b981', label: 'Issue (Weekly Pulse)' },
    { color: '#8b5cf6', label: 'Concept: AI Content' },
    { color: '#0ea5e9', label: 'Concept: Health Disinfo' },
    { color: '#ef4444', label: 'Concept: Disinformation' },
    { color: '#f59e0b', label: 'Concept: Elections' },
    { color: '#10b981', label: 'Concept: Climate' },
    { color: '#f97316', label: 'Concept: Migration' },
    { color: '#fbbf24', label: 'Sequence (next issue)' },
  ];
  var h = items.map(function(i) {
    return '<div class="r"><div class="d" style="background:' + i.color + '"></div>' + i.label + '</div>';
  }).join('');
  document.getElementById('legend').innerHTML = h;
}

function updateStats() {
  if (!cy) return;
  var vn = cy.nodes(':visible').length;
  var ve = cy.edges(':visible').length;
  document.getElementById('stats').textContent = vn + '/' + DATA.nodes.length + ' nodes · ' + ve + ' edges';
}

init();
</script>
</body>
</html>"""

with open(f"{WIKI}/viz.html", 'w') as f:
    f.write(viz_html)
print("  ✅ viz.html")

# Log file
print("📝 Generating log...")
from datetime import date

log_md = f"""# EDMO Pulse Wiki — Change Log

## [{date.today().isoformat()}] Initial Ingest
- Created wiki from EDMO Weekly Pulse archive
- {len(ARTICLES)} issues ingested
- Generated bundle.json ({len(nodes)} nodes, {len(edges)} edges)
- Generated viz.html
- Source: https://edmo.eu/pulse/
"""

log_path = f"{WIKI}/log.md"
if os.path.exists(log_path):
    print("  ⏭️ log.md exists (append manually — history preserved)")
else:
    with open(log_path, 'w') as f:
        f.write(log_md)
    print("  ✅ log.md")

# README
readme = f"""# EDMO Weekly Pulse Wiki

EDMO Weekly Pulse bültenlerinin wiki arşivi ve görselleştirmesi.

- **{len(ARTICLES)} sayı** (Mart - Eylül 2026)
- **Kaynak:** [EDMO Pulse](https://edmo.eu/pulse/)
- **Görselleştirme:** `viz.html` (Cytoscape.js)
- **Güncelleme:** Haftalık cronjob ile otomatik

## Yapı

```
raw/           — Her sayı için wiki sayfaları
entities/      — EDMO kurum sayfası
bundle.json    — Görselleştirme verisi
viz.html       — Etkileşimli grafik
index.md       — Ana sayfa
log.md         — Değişiklik kaydı
```
"""

with open(f"{WIKI}/README.md", 'w') as f:
    f.write(readme)
print("  ✅ README.md")

print(f"\n🎉 Done! Generated {len(ARTICLES)} articles + index + entity + bundle + viz")
