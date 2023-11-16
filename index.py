# app.py
import streamlit as st

def main():

    # Set the page width
    st.set_page_config(page_title="portfolio", layout="wide")

    # Title
    st.markdown("<h3>Student name </h3>",unsafe_allow_html=True)

    # Create a three-column layout with some spacing
    col1, col2, col3 = st.columns([3, 3, 3], gap="large")

    # Information in the left column
    with col1:
        # Align content to the left
        st.markdown('<div style="text-align: left; margin-left: 60px;">', unsafe_allow_html=True)

        st.write("Wissner-Slivka Chair")
        st.write("MacArthur Fellow")

        st.write("Office: 578 Allen Center")
        st.write("Fax: 206-685-2969")
        st.write("Email: [yejin@cs.washington.edu](mailto:yejin@cs.washington.edu)")

        # Close the alignment div
        st.markdown('</div>', unsafe_allow_html=True)



    # Contact Information in the middle column
    with col2:
        st.markdown('<div style="margin-top: -200px;">', unsafe_allow_html=True)
        st.write("Paul G. Allen School of Computer Science & Engineering")
        st.write("University of Washington")
        st.write("Box 352350")
        st.write("185 E Stevens Way NE")
        st.write("Seattle, WA 98195-2350")

        st.write("Allen Institute for Artificial Intelligence")
        st.write("2157 N Northlake Way, Suite 110")
        st.write("Seattle, WA 98103")

    # Image in the right column with spacing
    with col3:
        st.markdown('<div style="text-align: right; margin-right: 40px; margin-top: -300px;">', unsafe_allow_html=True)
        st.markdown("<h3>Image: </h3>",unsafe_allow_html=True)
        st.image("logo192.png", caption="Placeholder Image", use_column_width=False)
        # Close the alignment div
        st.markdown('</div>', unsafe_allow_html=True)
    

    st.subheader("News:")
    news_items = [
        "A TED talk: [Why AI is Incredibly Smart --- and Shockingly Stupid](https://www.google.com/)",
        "MacArthur Fellow (class of 2022); 2 min YouTube reel [here](#)",
        "Keynote at ACL: [2082: An ACL Odyssey: The Dark Matter of Language and Intelligence](#) along with a fireside chat on [The Trajectory of ACL and the Next 60 years](#) and a pre-recorded talk [here](#)",
        "An invited article, [The Curious Case of Commonsense Intelligence](#) for the Daedalus's special issue on AI & Society",
        "A podcast interview with the Gradient on [commonsense and morality](#)",
        "Featured by New Yorker: [Can Computers Learn Common Sense?](#)",
        "The TWIML AI Podcast with Sam Charrington on [Why is language the best medium for reasoning?](#)",
        "An interview by Dhruv Batra on [Humans of AI: Stories, Not Stats](#)",
        "Featured by NY Times on Delphi: [Can a Machine Learn Morality?](#)",
        "Promoted to a full professor as of Apr 2021, the new title effective on Sep 2021",
        "Endowed with the Brett Helsel Career Development Professorship (2020 - 2023)",
        "Won the AAAI Outstanding Paper Award 2020",
        "Featured by Quanta Magazine --- 🤖[Common Sense Comes Closer to Computers](#)🤖",
        "Our UW Sounding Board team is the winner of the Alexa Prize!",
        "Our UW team (with Pooja, Max, Ari) won the Facebook ParlAI award!"
        ]
    for item in news_items:
        st.markdown(f"- {item}", unsafe_allow_html=True)

        # Awards and Recognition
    st.subheader("Awards:")
    awards_items = [
            "Best Paper (Award) at ACL 2023",
            "Outstanding Paper (Award) at ACL 2023",
            "Outstanding Paper (Award) at ICML 2022",
            "Best Paper (Award) at NAACL 2022",
            "Outstanding Paper (Award) at NeurIPS 2021",
            "Outstanding Paper (Award) at AAAI 2020",
            "Marr Prize (Award) at ICCV 2013"
        ]

    for item in awards_items:
        award_text = item.replace("(Award)", "[Award](#)")
        st.write(f"    - {award_text}")


    # Test of Time:
    st.markdown("<h6>Test of Time:</h6>", unsafe_allow_html=True)

    test_of_time_items = [
        "[Longuet Higgins Prize](#) at CVPR 2021",
        "[Test of Time Award](#) at ACL 2021"
    ]

    for item in test_of_time_items:
        st.markdown(f"  \- {item}", unsafe_allow_html=True)
    
        # Finalists:
    st.markdown("<h6>Finalists:</h6>", unsafe_allow_html=True)
    finalists_items = [
        "IROS RoboCup Best Paper Finalist at IROS 2019",
        "Best Paper Nomination at ACL 2019"
    ]

    for item in finalists_items:
        st.markdown(f"\- {item}", unsafe_allow_html=True)

    # Recognition:
    st.markdown("<h2>Recognition:</h2>", unsafe_allow_html=True)
    recognition_items = [
    "[Distinguished Research Fellow](#) at the Institute for Ethics in AI at Oxford (2023)",
    "[Wissner-Slivka Chair](#) (2023 - current)",
    "[MacArthur Fellow](#) (2022)",
    "[ACL Fellow](#) (2022)",
    "[Brett Helsel Career Development Professorship](#) (2020 - 2023)",
    "[Borg Early Career Award (BECA)](#) (2018)",
    "[IEEE AI's 10 to Watch](#) (2016)"
    ]

    for item in recognition_items:
        st.markdown(f"- {item}", unsafe_allow_html=True)


    # Recent Talks (2018 - 2024):
    st.subheader("Recent Talks (2018 - 2024):")

    recent_talks = [
        "Mar 2024 - Keynote at the Weinberg [Cognitive Science Symposium](#)",
        "Mar 2024 - Colloquium at Harvard Psychology",
        "Nov 2023 - Visit at UC Irvine",
        "Nov 2023 - Talk at UCSD",
        "Nov 2023 - Colloquium at MIT Brain and Cognitive Sciences (BCS)",
        "Nov 2023 - Distinguished Lecture at UBC",
        "Oct 2023 - Talk at the MacArthur Fellows Forum",
        "Oct 2023 - Distinguished Lecture at TTIC",
        "Oct 2023 - Talk at the Ohio State University",
        "Sep 2023 - Talk at the Department of Philosophy at NYU",
        "Sep 2023 - Talk at Cornell Tech",
        "Sep 2023 - Talk at MSR @ NYC",
        "Aug 2023 - Keynote at VLDB",
        "Aug 2023 - Talk at the Simons Institute Workshop on LLMs with the recorded talk [here](#)",
        "Aug 2023 - Talk at Duolingo",
        "Jun 2023 - Keynote at CVPR"
    ]

    for talk in recent_talks:
        st.markdown(f"- {talk}", unsafe_allow_html=True)

    # Research Interests:
    st.subheader("Research Interests:")

    research_interests = """
    My primary research interests are in the fields of Natural Language Processing, Machine Learning, Artificial Intelligence, with broader interests in Computer Vision and Digital Humanities.

    Language and X ∈ {vision, knowledge, world, mind, society...} : Intelligent communication requires the ability to read between the lines and to reason beyond what is said explicitly. My recent research has been under two broad themes: 
    (i) learning the contextual, grounded meaning of language from various contexts in which language is used — both physical (e.g., visual) and abstract (e.g., social, cognitive), and 
    (ii) learning the background knowledge about how the world works, latent in large-scale multimodal data.

    More specifically, my research interests include:
    - Language Grounding with Vision: Learning semantic correspondences between language and vision at a very large scale, addressing tasks such as image captioning, multimodal knowledge learning, and reasoning.
    - Physical Commonsense Reasoning: Learning naive physics-type knowledge from language and other modalities; modeling action causality and entailment using frame semantic style representation.
    - Social Commonsense Reasoning and Connotation Frames: Modeling connotative implications of actions and events; modeling why people do (intent) what they do and the (emotional) causal impact of different actions and events.
    - Language Generation and Conversational AI: Modeling the long-term context; tracking and simulating the world represented in a story or a narrative; learning to write; integrating physical and social commonsense in storytelling.
    - AI for Social Good: Fake review / news detection; political fact-checking; identifying unwanted bias in modern films and literature.
    """

    st.markdown(research_interests)
   
    # Recent Preprints:
    st.subheader("Recent Preprints:")

    # Recent Preprints:
    # Recent Preprints:
    st.subheader("Recent Preprints:")

    preprints = [
        {
            "title": "The Generative AI Paradox: 'What It Can Create, It May Not Understand'",
            "name": "Peter West, Ximing Lu, Nouha Dziri, Faeze Brahman, Linjie Li, Jena D. Hwang, Liwei Jiang, Jillian Fisher, Abhilasha Ravichander, Khyathi Chandu, Benjamin Newman, Pang Wei Koh, Allyson Ettinger, Yejin Choi",
            "arxiv_link": "arXiv:452544",
            "link":"google.com"
        },
        {
            "title": "Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties",
            "name": "Taylor Sorensen, Liwei Jiang, Jena Hwang, Sydney Levine, Valentina Pyatkin, Peter West, Nouha Dziri, Ximing Lu, Kavel Rao, Chandra Bhagavatula, Maarten Sap, John Tasioulas, Yejin Choi",
            "arxiv_link": "arXiv:2309.00779",
             "link":"google.com"
        },
        # Add other papers in a similar format
    ]

    for paper in preprints:
        st.markdown(f" **[{paper['title']}]({paper['link']})**\n{paper['name']}")
        st.write(f"{paper['arxiv_link']}")


    # Recent Publications (2016 - 2023):
    st.subheader("Recent Publications (2016 - 2023):")

    publications = [
        {
            "title": "Faith and Fate: Limits of Transformers on Compositionality",
            "authors": "Nouha Dziri, Ximing Lu, Melanie Sclar, Xiang Lorraine Li, Liwei Jiang, Bill Yuchen Lin, Peter West, Chandra Bhagavatula, Ronan Le Bras, Jena D. Hwang, Soumya Sanyal, Sean Welleck, Xiang Ren, Allyson Ettinger, Zaid Harchaoui, Yejin Choi",
            "conference": "NeurIPS 2023",
            "presentation": "spotlight",
            "source_link": "https://example.com/source2",
        },
        # Add other publications in a similar format
    ]

    for publication in publications:
        st.markdown(
            f" **[{publication['title']}]({publication['source_link']})** - {publication['authors']} ({publication['conference']} {publication['presentation']})"
        )
        st.write("")  # Add an empty line for separation

    # Full List of Publications:
    st.subheader("Full List of Publications:")

    # Hyperlink for Google Scholar
    st.markdown(" [Google Scholar](https://scholar.google.com/citations?user=YOUR_GOOGLE_SCHOLAR_ID)")

    # Hyperlink for Semantic Scholar
    st.markdown("[Semantic Scholar](https://www.semanticscholar.org/author/YOUR_SEMANTIC_SCHOLAR_ID)")



    # Recent Teaching:
    st.subheader("Recent Teaching:")

    teaching_points = [
        {
            "course_code": "CSE 599 D1",
            "course_type": "(Grad)",
            "course_title": "Exploration on Language, Knowledge, and Reasoning",
            "term": "[Winter 2023]",
            "source_link": "https://example.com/course1",
        },
        {
            "course_code": "CSEP 517",
            "course_type": "(Professional MS)",
            "course_title": "Natural Language Processing",
            "term": "[Winter 2021]",
            "source_link": "https://example.com/course2",
        },
        # Add other teaching points in a similar format
    ]

    for point in teaching_points:
        st.markdown(
            f"[{point['course_code']} {point['course_type']} - {point['course_title']} {point['term']} ]({point['source_link']})"
        )


    st.title("xlab:")
    # Current members:
    st.markdown("\t<h4>Current members:</h4>",unsafe_allow_html=True)


    post_doc_members = [
        "Sean Welleck (Postdoc/Young Investigator @ UW/AI2 -> ✨starting his tenure-track at CMU in Jan 2024)",
        "Lianhui (Karen) Qin (Young Investigator @ AI2 -> ✨starting her tenure-track at UCSD in 2024)",
        "Yuntian Deng (Young Investigator @ AI2 -> ✨starting his tenure-track at Waterloo in 2024)",
        "Mitchell L Gordon (Postdoc @ AI2 -> ✨starting his tenure-track at MIT in 2024) --- co-advised with Jeff Heer",
        "Fatemeh (Niloofar) Mireshghallah (Postdoc @ UW) - co-advised with Yulia Tsvetkov",
        "Tianxiao Shen (Postdoc @ UW) - co-advised with Zaid Harchaoui",
        "Abhilasha Ravichander (Young Investigator @ AI2)",
        "Faeze Brahman (Young Investigator @ AI2)",
        "Valentina Pyatkin (Young Investigator @ AI2)",
        "Hyunwoo Kim (Young Investigator @ AI2)",
    ]

    phd_members = [
        "Peter West",
        "Xiujun Li",
        "Jae Sung (James) Park - co-advised with Ali Farhadi",
        "Liwei Jiang",
        "Alisa Liu - co-advised with Noah Smith",
        "Jiacheng (Gary) Liu - co-advised with Hannaneh Hajishirzi",
        "Jillian Fisher - co-advised with Zaid Harchaoui",
        "Melanie Sclar - co-advised with Yulia Tsvetkov",
        "Jaehun Jung",
        "Taylor Sorensen",
        "Ximing (Gloria) Lu",
        "Ben Newman",
        "Anas Awadalla - co-advised with Ludwig Schmidt",
        "Linjie (Lidsey) Li",
    ]

    # Display post-doc members
    st.subheader("Post Doc:")
    for member in post_doc_members:
        st.markdown(f"\t {member}", unsafe_allow_html=True)

    # Display PhD members
    st.subheader("PhD:")
    for member in phd_members:
        st.markdown(f"\t {member}")


    # Title
    st.title("Former Members")

    # Post Doc section
    st.subheader("Post Doc:")
    post_doc_members = [
        "Nouha Dziri (-> Research Scientist @ AI2)",
        "Yuchen (Bill) Lin (-> Research Scientist @ AI2)",
        "Prithviraj Ammanabrolu (-> Assistant Professor at UCSD after a gap year at MosaicML)",
        "Alane Suhr (-> Assistant Professor @ UC Berkeley)",
        "Xiang Lorraine Li (-> Assistant Professor @ University of Pittsburgh)",
        "Youngjae Yu (-> Assistant Professor @ Yonsei University)",
        "Daniel Khashabi (-> Assistant Professor @ JHU)",
        "Swabha Swayamdipta (-> Assistant Professor @ USC)",
        "Vered Shwartz (-> Assistant Professor @ UBC)",
        "Jack Hessel (-> Research Scientist @ AI2 -> Samaya AI)",
        "Rachel Rudinger (-> Assistant Professor @ University of Maryland)",
        "Yonatan Bisk (-> Assistant Professor @ CMU LTI/Robotics)",
        "Jan Buys (-> Assistant Professor @ University of Cape Town)",
        "Yannis Konstas (-> Assistant Professor @ Heriot-Watt University)"
    ]

    # Display post-doc members as bullet points
    for member in post_doc_members:
        st.write(f"   {member}")

    # PhD section
    st.subheader("PhD:")
    phd_members = [
        "Saadia Gabriel (->Assistant Professor @ UCLA after a gap year at MIT and NYU)",
        "Maarten Sap (-> Assistant Professor at CMU)",
        "Rowan Zellers (-> OpenAI)",
        "Maxwell Forbes (-> Wandering around the world)",
        "Antoine Bosselut (-> Assistant Professor @ EPFL)",
        "Hannah Rashkin (-> Research Scientist @ Google Research)",
        "Eunsol Choi (-> Assistant Professor @ Texas Austin)",
        "Chloé Kiddon (-> Google)",
        "Jun Seok Kang (-> Blink Health)",
        "Song Feng (-> Research Staff Member @ IBM Research)",
        "Polina Kuznetsova (-> Research Scientist @ Facebook)",
        "Ritwik Banerjee (-> Research Assistant Professor @ Stony Brook University)"
    ]

    # Display PhD members as bullet points
    for member in phd_members:
        st.write(f"   {member}")

    st.markdown("<h4>Short Bio:</h4>",unsafe_allow_html=True) 
    short_bio = "Yejin Choi is Wissner-Slivka Professor at the Paul G. Allen School of Computer Science & Engineering at the University of Washington and also a senior research director at AI2 overseeing the project Mosaic. Her research investigates a wide variety of problems across NLP and AI, including commonsense knowledge and reasoning, neural language (de-)generation, language grounding with vision and experience, and AI for social good. She is a MacArthur Fellow and a co-recipient of the NAACL Best Paper Award in 2022, the ICML Outstanding Paper Award in 2022, the ACL Test of Time award in 2021, the CVPR Longuet-Higgins Prize (test of time award) in 2021, the NeurIPS Outstanding Paper Award in 2021, the AAAI Outstanding Paper Award in 2020, the Borg Early Career Award (BECA) in 2018, the inaugural Alexa Prize Challenge in 2017, IEEE AI's 10 to Watch in 2016, and the ICCV Marr Prize (best paper award) in 2013. She received her Ph.D. in Computer Science at Cornell University and BS in Computer Science and Engineering at Seoul National University in Korea."
    # Display the short bio using Streamlit
    st.text(short_bio)
    
    st.markdown("<h4>Personal:</h4>",unsafe_allow_html=True)
    personal="scuba!"
    st.text(personal)















if __name__ == "__main__":
    main()
