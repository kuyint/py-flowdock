# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    	= 
SPHINXMODBUILD	= sphinx-apidoc
MODULEDESTDIR	= ./
SPHINXBUILD   	= sphinx-build
SPHINXPROJ    	= ../flowdock
SOURCEDIR     	= ./
BUILDDIR      	= _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

build:
	@$(SPHINXMODBUILD) -o "$(MODULEDESTDIR)" "$(SPHINXPROJ)"
	@$(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)"

.PHONY: build
