export_req :
	@pip3 freeze > requirements.txt
	@echo "Export requirements.txt"
	@cat requirements.txt

import_req :
	@pip3 install -r requirements.txt
	@echo "Import requirements.txt"
	@cat requirements.txt

uninstall_lib :
	@pip3 uninstall -r requirements.txt
	@echo "Uninstall all libraries requirements.txt"
	@cat requirements.txt
	@pip3 freeze > requirements.txt
