import streamlit as st
from PIL import Image
import base64

def show_about():
    # Add background color using CSS
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #e0f7fa;  /* Light cyan background */
        }
        .team-member {
            background-color: #B2EBF2;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            text-align: center;
        }
        .team-member img {
            border-radius: 10px;
            margin-bottom: 10px;
            width: 150px;  /* Fixed width */
            height: 150px; /* Fixed height */
            object-fit: cover;  /* Maintain aspect ratio, cover the area */
        }
        .team-member ul {
            list-style-type: none;
            padding: 0;
            display: block;
            margin: 0;
        }
        .team-member ul li {
            display: block;
            margin: 5px 0;
        }
        .team-member a {
            text-decoration: none;
            color: #007bff;
        }
        .about-section {
            background-color: #B2EBF2;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("Tentang")
    st.markdown("""
    <div class="about-section">
        <p>
            Generative Adversarial Networks(GAN), merupakan sebuah jenis kerangka pembelajaran mesin yang diciptakan oleh Ian Goodfellow dan timnya pada tahun 2014. GAN terdiri dari dua jaringan saraf utama, yaitu generator dan diskriminator. Generator bertugas menciptakan data palsu, sedangkan diskriminator menilai keaslian data tersebut dengan membandingkannya dengan data nyata, memberikan masukan kepada generator.
        </p>
        <p>
            Web ini adalah contoh penerapan GAN untuk menggenerate sebuah gambar sederhana dengan pemrograman python.
        </p>
        <p>
            Anda dapat mencobanya dengan mengunggah gambar dan mengklik 'Generate' di halaman home. GAN memiliki beragam aplikasi, mulai dari pembuatan foto realistis hingga seni kreatif, bahkan hingga desain molekul baru untuk penemuan obat.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.header("Anggota Tim")
    
    # List of team members
    team_members = [
        {
            "name": "M.Iqbal",
            "activity_id": "9064101",
            "image": "foto/iqbal.jpg",
            "social_links": {
                "Instagram": "https://www.instagram.com/ahmad.iqbal11/"
            }
        },
        {
            "name": "Nabila",
            "activity_id": "7965781",
            "image": "foto/nabila.jpg",
            "social_links": {
                "Instagram": "https://www.instagram.com/nab2la/"
            }
        },
        {
            "name": "Angelica",
            "activity_id": "9299435",
            "image": "foto/angelica.jpg",
            "social_links": {
                "Instagram": "https://www.instagram.com/ngelica.my/"
            }
        },
        {
            "name": "Eneng",
            "activity_id": "8768551",
            "image": "foto/eneng.jpg",
            "social_links": {
                "Instagram": "https://www.instagram.com/bubbleblack8_/"
            }
        },
        {
            "name": "Dhona",
            "activity_id": "7681059",
            "image": "foto/dhona.jpg",
            "social_links": {
                "Instagram": "https://www.instagram.com/iadho__/"
            }
        },
        {
            "name": "Endah",
            "activity_id": "8687845",
            "image": "foto/endah.jpg",
            "social_links": {
                "Instagram": "https://www.instagram.com/endah_rosanti21/"
            }
        },
    ]

    # Display team members in columns
    cols = st.columns(3)  # Create 3 columns per row for better layout

    for index, member in enumerate(team_members):
        col = cols[index % 3]  # Ensure that only 3 columns are filled per row
        with col:
            st.markdown(f"""
            <div class="team-member">
                <h3>{member['name']}</h3>
                <p>ID Kegiatan: {member['activity_id']}</p>
                <img src="data:image/jpeg;base64,{base64.b64encode(open(member['image'], 'rb').read()).decode()}" width="100%">
                <h4>Social Media</h4>
                <ul>
                    {" ".join([f'<li><a href="{link}" target="_blank">{platform}</a></li>' for platform, link in member['social_links'].items()])}
                </ul>
            </div>
            """, unsafe_allow_html=True)

        # Add a new row after every 3 members
        if (index + 1) % 3 == 0 and (index + 1) < len(team_members):
            cols = st.columns(3)