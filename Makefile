watch-vscode:
	@: ; \
		echo "Watching vscode..." ; \
		prev=0; \
		while true; do \
			latest=$$( $(MAKE) latest-time) ; \
			: echo "Latest: $$latest, prev: $$prev" ; \
			[ $${prev} -eq $${latest} ] && sleep 1 && continue ; \
			clear ; \
			echo ; \
			date ; \
			$(MAKE) gray ; \
			python3 solution.py && $(MAKE) green || $(MAKE) red ; \
			prev=$$latest; \
		done;

test:
	python3 solution.py

latest-time:
	@find . -type f -name "*.py" -exec stat -f %Sm  -t %s {} \; | sort -r | head -n1

green:
	@mkdir -p .vscode
	@echo '{"workbench.colorCustomizations": {"statusBar.background": "#029400", "statusBar.noFolderBackground": "#029400", "statusBar.debuggingBackground": "#029400", "activityBar.background": "#014400" }}'	> .vscode/settings.json
red:
	@mkdir -p .vscode
	@echo '{"workbench.colorCustomizations": {"statusBar.background": "#940000", "statusBar.noFolderBackground": "#940000", "statusBar.debuggingBackground": "#940000", "activityBar.background": "#440000" }}'	> .vscode/settings.json
gray:
	@mkdir -p .vscode
	@echo '{"workbench.colorCustomizations": {"statusBar.background": "#808080", "statusBar.noFolderBackground": "#808080", "statusBar.debuggingBackground": "#808080", "activityBar.background": "#404040" }}'	> .vscode/settings.json
