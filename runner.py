# Author: Sakthi Santhosh
# Created on: 25/08/2023
def main() -> None:
    from lib import app_handle

    app_handle.run(debug=False, host="0.0.0.0")

if __name__ == "__main__":
    main()
