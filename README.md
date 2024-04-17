# omniflow

[![Tests][badge-tests]][link-tests]
[![Documentation][badge-docs]][link-docs]

[badge-tests]: https://img.shields.io/github/actions/workflow/status/sysbio-curie/omniflow/test.yaml?branch=main
[link-tests]: https://github.com/sysbio-curie/omniflow/actions/workflows/test.yml
[badge-docs]: https://img.shields.io/readthedocs/omniflow
[link-docs]: https://omniflow.readthedocs.io

Package to extract, visualize, convert and study interactions from database into executable activity flow based model.
Omniflow (temporary name), is based on Omnipath (https://github.com/saezlab/omnipath), pypath (https://github.com/saezlab/pypath) and Atopo (https://github.com/druglogics/atopo).

This is a work-in-progress package made in collaboration with Dénes Turei and Asmund Flobak.

ROADMAP:

version 0.1.0
 <ul>
  <li>Network core object to store nodes and edges</li>
  <li>Inputs methods: list of nodes, sif file</li>
  <li>Enrichment methods: Shortest path (pypath)</li>
  <li>Resources: Omnipath (All interactions)</li>
  <li>Output formats: bnet file</li>
</ul>
