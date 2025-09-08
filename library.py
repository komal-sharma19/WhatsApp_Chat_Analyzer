import subprocess
import sys

def get_and_install_library_versions():
    """
    Finds and prints the installed versions of specified Python libraries.
    If a library is not installed, it attempts to install it using pip.
    """
    libraries = {
        "streamlit": "streamlit",
        "urlextract": "urlextract",
        "pandas": "pandas",
        "numpy": "numpy",
        "matplotlib": "matplotlib",
        "wordcloud": "wordcloud",
        "emoji": "emoji",
        "gunicorn": "gunicorn"
    }
    
    print("--- Environment Information ---")
    # Print Python version here
    print(f"Python Version: {sys.version.splitlines()[0]}") # Gets the first line of sys.version
    print("-------------------------------")

    print("--- Library Versions & Installation Status ---")
    for lib_name, import_name in libraries.items():
        try:
            # Attempt to import the library
            lib = __import__(import_name)
            version = lib.__version__
            print(f"{lib_name}: {version} (Installed)")
        except ImportError:
            print(f"{lib_name}: Not installed. Attempting to install...")
            try:
                # Use subprocess to run pip install
                # sys.executable gets the path to the current Python interpreter
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib_name])
                print(f"{lib_name}: Successfully installed.")
                # After successful installation, try to import again to get the version
                try:
                    lib = __import__(import_name)
                    version = lib.__version__
                    print(f"{lib_name}: {version} (Newly Installed)")
                except AttributeError:
                    print(f"{lib_name}: Newly installed, but version information not directly available via __version__.")
                except Exception as e:
                    print(f"{lib_name}: Newly installed, but error retrieving version - {e}")
            except subprocess.CalledProcessError as e:
                print(f"Error installing {lib_name}: {e}. Please try installing manually: pip install {lib_name}")
            except Exception as e:
                print(f"An unexpected error occurred during installation of {lib_name}: {e}")
        except AttributeError:
            print(f"{lib_name}: Installed, but version information not directly available via __version__.")
        except Exception as e:
            print(f"{lib_name}: Error retrieving version - {e}")
    print("------------------------------------------")

# Call the function
get_and_install_library_versions()