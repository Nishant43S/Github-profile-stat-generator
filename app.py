import streamlit as st
from streamlit_option_menu import option_menu
from bs4 import BeautifulSoup
import requests

def insert_css(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

def insert_html(html_file):
    with open(html_file) as f:
        return st.markdown(
            f.read(),unsafe_allow_html=True
        )


st.set_page_config(
    page_title="profile stats generator",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

#### app functions

def ReadMe_card_web(github_url)->list:
    try:
        url = requests.get(f"https://github.com/{github_url}?tab=repositories")
        
        ### checking responce
        if url.status_code == 200:
            soup = BeautifulSoup(url.content,"lxml")

            repo_lis = [] ### repositories list
            repo_name = soup.find_all("h3",class_="wb-break-all")
            for i in repo_name:
                repo_lis.append((i.text.strip().replace("Public","").replace("\n","")))

            return repo_lis

    except Exception as e:
        st.warning("Error...\n\n",e,icon="⚠️")


def Layout_border(border):
    if border:
        return "false"
    else:
        return "true"

class ProfileStats:

    def Visitors_Count(self,username):
        """
        github profile visitors
        count batch
        """
        self.username = username


        try:
            if username.strip() != "":
                Visitor_count = f"""
                <p align="left"> 
                    <img 
                        src="https://komarev.com/ghpvc/?username={username}&label=Profile%20views&color=0e75b6&style=flat" 
                        alt="{username}"
                    /> 
                </p>
                """
                st.markdown(Visitor_count,unsafe_allow_html=True)

                st.text("")
                st.write("Visitors Count code")
                st.code(Visitor_count,wrap_lines=False)
                
                st.text("")
                st.write("---")
            else:
                st.warning(body="Enter User Name",icon="✏️")


        except Exception as e:
            st.warning('Error...\n\n',e,icon="⚠️")

    
    def Profile_Statstics(self,username,theme,addborder):
        """
        displaying profile statstics
        """

        st.text("")

        self.username = username
        self.theme = theme
        self.addborder = addborder

        try:
            if username.strip() != "":
                
                self.profile_statstics = f"""
                ![{username} GitHub stats](https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&theme={theme}&hide_border={Layout_border(addborder)})
                """

                st.write(self.profile_statstics)
                
            
        except Exception as e:
            st.warning('Error...\n\n',e,icon="⚠️")

    def profile_statstics_code(self):
        
        st.text("")
        st.write("profile statstics code")
        st.code(self.profile_statstics,wrap_lines=False)
        st.text("")
        st.write("---")

    
    def Languages_statstics(self,username,addborder,theme,layout):
        """
        language used statstics
        """
        st.text("")

        self.username = username
        self.theme = theme
        self.addborder = addborder
        self.layout = layout

        try:
            if username.strip() != "":
                self.language_stat = f"""
                ![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username={username}&hide_progress=false&theme={theme}&layout={layout}&hide_border={Layout_border(addborder)})
                """

                st.write(self.language_stat)

        except Exception as e:
            st.warning('Error...\n\n',e,icon="⚠️")
    

    def language_statstics_code(self):
        
        st.text("")
        st.write("language statstics code")
        st.code(self.language_stat,wrap_lines=False)
        st.text("")
        st.write("---")
    
    def Profile_streak(self,username,theme,addborder):
        """
        displaying profile streak
        """

        st.text("")

        self.username = username
        self.theme = theme
        self.addborder = addborder

        
        try:
            if username.strip() != "":
                
                self.profile_streak = f"""
                <img  
                    src="https://streak-stats.demolab.com?user={username}&locale=en&mode=daily&theme={theme}&hide_border={Layout_border(addborder)}&border_radius=5&order=3"
                    height="170" alt="streak graph" 
                 />
                """

                st.markdown(self.profile_streak,unsafe_allow_html=True)
                
            
        except Exception as e:
            st.warning('Error...\n\n',e,icon="⚠️")

    def profile_streak_code(self):
        
        st.text("")
        st.write("profile streak code")
        st.code(self.profile_streak,wrap_lines=False)
        st.text("")
        st.write("---")




App_sidebar = st.sidebar ### creating side bar

with App_sidebar:
    st.text("")
    st.subheader("Developer: Nishant Maity")
    st.text("")

    Main_menu = option_menu(
        menu_title="",
        options=["Stats Generator","App Info"],
        icons=["bar-chart","person-circle"],
        default_index=0
    )

    st.text("")

    if Main_menu == "Stats Generator":
        ### visitor count check box
        visitor_count_box = st.checkbox(
            label="Visitors count batch",
            value=True,key="Visitor count batch",
            label_visibility="visible"
        )

        ### profile statstics check box
        profile_statstics_box = st.checkbox(
            label="Profile Statstics",
            value=True,key="profile statstics",
            label_visibility="visible"
        )

        ### language statstics check box
        language_statstics_box = st.checkbox(
            label="Language Statstics",
            value=False,key="language statstics",
            label_visibility="visible"
        )

        ### profile streak check box
        profile_streak_box = st.checkbox(
            label="Profile Streak",
            value=False,key="profile streak",
            label_visibility="visible"
        )

        ### readme statstics check box
        readme_stat_box = st.checkbox(
            label="Repositories Statstics",
            value=False,key="readme statsics",
            label_visibility="visible"
        )


### main app
if Main_menu == "Stats Generator":

    ## creating column
    Blank_appcol1, App_column, Blank_appcol2 = st.columns([2,8,2],gap="small")

    with Blank_appcol1:
        pass

    with Blank_appcol2:
        pass

    stats = ProfileStats()

    with App_column:
        st.subheader("Github Profile Stats Generator")

        ## taking username input
        User_Input = st.text_input(
            label="Enter Your Github profile username",
            value="Nishant43S",
            key="userinput",
            type="default"
        )

        UserName_Input = User_Input.lower()

        st.text("")

        ### visitors count
        if visitor_count_box:
            if __name__=="__main__":
                stats.Visitors_Count(username=UserName_Input)

        ## profile satastics
        if profile_statstics_box:
            if UserName_Input.strip() != "":

                ### creating statstics columns
                Stat_Theme_col, stat_display_col = st.columns(2,gap="small")

                with Stat_Theme_col:
                    st.text("")
                    
                    Statstics_border = st.toggle(
                        label="Border",
                        value=False,
                        key="statstics border"
                    )

                    Statstics_theme = st.selectbox(
                        label="Select Theme",
                        options=["dark", "radical", "merko",
                                "gruvbox", "tokyonight", "onedark", 
                                "cobalt", "synthwave", "highcontrast", "dracula",
                                "light"
                            ],
                        key="Statstics Theme",
                        index=4
                    )

                
                with stat_display_col:
                    if __name__=="__main__":
                        stats.Profile_Statstics(
                            username=UserName_Input,
                            theme=Statstics_theme,
                            addborder=Statstics_border
                        )

                if __name__=="__main__":
                    stats.profile_statstics_code()
            
            else:
                st.warning(body="Enter User Name",icon="✏️")

        ### language statstics
        if language_statstics_box:
            if UserName_Input.strip() != "":
                Lang_theme_col, Lang_display_col = st.columns(2,gap="small")

                with Lang_theme_col:
                    st.text("")
                    lang_Statstics_border = st.toggle(
                        label="Border",
                        value=False,
                        key="language statstics border"
                    )

                    Lang_Statstics_theme = st.selectbox(
                        label="Select Theme",
                        options=["dark", "radical", "merko",
                                "gruvbox", "tokyonight", "onedark", 
                                "cobalt", "synthwave", "highcontrast", "dracula","light"
                            ],
                        key="Lang Statstics Theme",
                        index=4
                    )

                    Lang_Layout_theme = st.selectbox(
                        label="Select Layout",
                        options=["compact", "donut", "donut-vertical",
                                "pie"
                            ],
                        key="Lang layout Theme",
                        index=0
                    )
                
                with Lang_display_col:
                    if __name__=="__main__":
                        stats.Languages_statstics(
                            username=UserName_Input,
                            addborder=lang_Statstics_border,
                            theme=Lang_Statstics_theme,
                            layout=Lang_Layout_theme
                        )
                
                if __name__=="__main__":
                    stats.language_statstics_code()
                    
            else:
                st.warning(body="Enter User Name",icon="✏️")

        ## profile satastics
        if profile_streak_box:
            if UserName_Input.strip() != "":

                ### creating statstics columns
                Streak_Theme_col, streak_display_col = st.columns(2,gap="small")

                with Streak_Theme_col:
                    st.text("")
                    
                    Streak_border = st.toggle(
                        label="Border",
                        value=False,
                        key="streak border"
                    )

                    Streak_theme = st.selectbox(
                        label="Select Theme",
                        options=["dark", "radical", "merko",
                                "gruvbox", "tokyonight", "onedark", 
                                "cobalt", "synthwave", "highcontrast", "dracula",
                                "light"
                            ],
                        key="streak Theme",
                        index=4
                    )
                
                with streak_display_col:
                    if __name__=="__main__":
                        stats.Profile_streak(
                            username=UserName_Input,
                            theme=Streak_theme,
                            addborder=Streak_border
                        )

                if __name__=="__main__":
                    stats.profile_streak_code()

            else:
                st.warning(body="Enter User Name",icon="✏️")

        if readme_stat_box:
            if UserName_Input.strip() != "":

                ### creating statstics columns
                readmestat_Theme_col, readmestat_display_col = st.columns(2,gap="small")

                with readmestat_Theme_col:
                    st.text("")

                    readme_stat_border = st.toggle(
                        label="Border",
                        value=False,
                        key="readme stat border"
                    )

                    readme_stat_theme = st.selectbox(
                        label="Select Theme",
                        options=["dark", "radical", "merko",
                                "gruvbox", "tokyonight", "onedark", 
                                "cobalt", "synthwave", "highcontrast", "dracula",
                                "light"
                            ],
                        key="readme stat Theme",
                        index=4
                    )

                    repositories_name = st.selectbox(
                        label="Select repository",
                        options=ReadMe_card_web(User_Input),
                        key="repositories name"
                    )
                
                with readmestat_display_col:
                    if __name__=="__main__":
                        st.text("")

                        repo_stats = f"[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username={UserName_Input}&repo={repositories_name}&theme={readme_stat_theme}&hide_border={Layout_border(readme_stat_border)})](https://github.com/{User_Input}/{repositories_name})"

                        st.write(repo_stats)
                if __name__=="__main__":
                    st.text("")
                    st.write("repo statstics code")
                    st.code(repo_stats)
        
        check_box_list = [
            readme_stat_box,profile_streak_box,
            language_statstics_box,visitor_count_box,
            profile_statstics_box
        ]

        if not any(check_box_list):
            st.success("press any checkbox",icon="☑️")


if __name__=="__main__":
    insert_css("cssfiles/app.css")

if Main_menu == "App Info":
    if __name__=="__main__":
        insert_html("app-info.html")

        

            
    