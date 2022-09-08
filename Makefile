SHELL:=/bin/bash

#CUSTOM_GNUPG_HOME:=$$(mktemp -d)
CUSTOM_GNUPG_HOME:=~/.gnupg

all: clean generate-key sign

# -- Sign and verify --
sign: prepare
	ANSIBLE_SIGN_GPG_PASSPHRASE="$$(cat keys.json | jq .passphrase -r)" \
		./venv/bin/ansible-sign --debug project gpg-sign \
			--gnupg-home $(CUSTOM_GNUPG_HOME) .

verify: prepare
	./venv/bin/ansible-sign --debug project gpg-verify \
		--gnupg-home $(CUSTOM_GNUPG_HOME) .

prepare: generate-key kill-gpg-agent

kill-gpg-agent:
	killall gpg-agent || true

# -- Generate the key --
generate-key: virtualenv
	if [ ! -f keys.json ]; then \
		./venv/bin/python ansible_sign_gen_key.py > keys.json; \
		make import-key; \
	fi

list-keys:
	gpg --homedir $(CUSTOM_GNUPG_HOME) --list-secret-keys

import-key:
	cat keys.json | jq .secret_key -r | \
		gpg --homedir $(CUSTOM_GNUPG_HOME) --import --batch --passphrase $$(cat keys.json | jq .passphrase -r) $${SECRET_KEY_FILE_PATH}

# -- Other --
virtualenv:
	@if [ ! -d venv ]; then \
		echo "# -- Creating virtualenv..."; \
		virtualenv -p python3 venv; \
		. ./venv/bin/activate && pip install -r requirements.txt; \
	fi

clean:
	rm -rf venv/
	rm -f keys.json
	rm -rf .ansible-sign/
