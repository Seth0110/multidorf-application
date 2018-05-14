# from bs4 import BeautifulSoup
from datetime import date


def list_df():
    # f = urllib.request.urlopen('http://bay12games.com/dwarves/older_versions.html')
    # soup = BeautifulSoup(f.read(), 'html.parser')
    # return soup.body.find('p', attrs={'class':'menu'}).text
    """For now we are hardcoding this in, and we only have a single version.  This is not the final behavior"""
    return [dict(
        version='0.44.10',
        date=date(2018, 5, 5),
        x86=dict(
            windows='http://bay12games.com/dwarves/df_44_10_legacy32.zip',
            windows_legacy='http://bay12games.com/dwarves/df_44_10_win32.zip',
            linux='http://bay12games.com/dwarves/df_44_10_linux32.tar.bz2',
            mac='http://bay12games.com/dwarves/df_44_10_osx32.tar.bz2'),
        x86_64=dict(
            windows='http://bay12games.com/dwarves/df_44_10_win.zip',
            windows_legacy='http://bay12games.com/dwarves/df_44_10_legacy.zip',
            linux='http://bay12games.com/dwarves/df_44_10_linux.tar.bz2',
            mac='http://bay12games.com/dwarves/df_44_10_osx.tar.bz2'))]
