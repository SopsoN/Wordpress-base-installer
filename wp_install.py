import os
import sys
import shutil

git_clone = "git clone "

def get_wp(wp_dir):
    wp_git = "https://github.com/WordPress/WordPress.git "

    print("\n@ Getting Wordpress @\n")

    os.system("wget https://wordpress.org/latest.tar.gz")
    os.system("tar -xzvf latest.tar.gz")
    shutil.move("wordpress", wp_dir)
    os.system("rm -rf latest.tar.gz")

    print("\n____ WORDPRESS DONE ____\n")

def get_git_plugins(wp_dir):
    git_plugins = []
    git_plugins.append("https://SopsoN@bitbucket.org/collegium/mc-serverstatus.git")
    git_plugins.append("https://SopsoN@bitbucket.org/SopsoN/wp-wheel-of-fortune.git")

    print("\n@ Getting Git WP plugins @\n")

    plugins_dir = wp_dir+"/wp-content/plugins/"

    os.chdir(plugins_dir)

    for plugin in git_plugins:
        print("\nGetting -> "+plugin+"\n")
        os.system(git_clone+plugin)

    os.chdir("../../..")

    print("\n____ Git WP plugins DONE ____\n")

def get_wp_plugins(wp_dir):
    wp_plugins = []
    wp_plugins.append("all-in-one-wp-migration")
    wp_plugins.append("contact-form-7")
    wp_plugins.append("creare-eu-cookie-law-banner")
    wp_plugins.append("duplicate-page")
    wp_plugins.append("easy-wp-smtp")
    wp_plugins.append("flamingo")
    wp_plugins.append("query-monitor")
    wp_plugins.append("woocommerce")
    wp_plugins.append("woocommerce-autocomplete-order")
    wp_plugins.append("woocommerce-pdf-invoices")
    wp_plugins.append("wordpress-seo")

    print("\n@ Getting plugins from Wordpress.org @\n")

    plugins_dir = wp_dir+"/wp-content/plugins/"

    os.chdir(plugins_dir)

    for plugin in wp_plugins:
        print("\nDownloading -> "+plugin+".zip\n")

        os.system("curl -O \"https://downloads.wordpress.org/plugin/"+plugin+".zip\"")

        print("\n...Unziping\n")
        os.system("unzip "+plugin+".zip")

    os.system("rm -rf *.zip")
    os.chdir("../../..")
    print("\n____ WP PLUGINS DONE ____\n")

def main():
    install_dirs = ["./wordpress"]
    os.system("clear")
    print("---- INSTALLATION ----")

    if len(sys.argv) > 1:
        install_dirs = sys.argv

    for wp_dir in install_dirs:
        if wp_dir == sys.argv[0]:
            continue

        get_wp(wp_dir)
        get_git_plugins(wp_dir)
        get_wp_plugins(wp_dir)

    print("\n---- END OF INSTALLATION ----")

main()
