

```python
import pandas as pd
from itables import init_notebook_mode
from itables import show

init_notebook_mode(all_interactive=True)

path_data='/home/eva/FAIRplus/tooling/WP3_FAIR_tooling/tool_discovery/outputs/ETL/tools_aggregation.tsv'
df = pd.read_csv(path_data, sep='\t')
df =df[:5]

show(df, scrollY="400px", scrollCollapse=True, paging=False)
```


    <IPython.core.display.Javascript object>



<div><table id="60b6c368-6578-4177-a8e0-0300b711eef6" class="display"><thead>
    <tr style="text-align: right;">
      
      <th>name</th>
      <th>description</th>
      <th>type</th>
      <th>topic</th>
      <th>input</th>
      <th>output</th>
    </tr>
  </thead></table>
<script type="text/javascript">
require(["datatables"], function (datatables) {
    $(document).ready(function () {
        var dt_args = {"scrollY": "400px", "scrollCollapse": true, "paging": false, "columnDefs": [{"width": "70px", "targets": "_all"}], "data": [["cabnet", "CABNet is a category Attention Block for Imbalanced Diabetic Retinopathy Grading", "['Script']", "[{'term': 'Imaging', 'uri': 'http://edamontology.org/topic_3382'}, {'term': 'Machine learning', 'uri': 'http://edamontology.org/topic_3474'}]", "[]", "[]"], ["rmea", "An R package to assess nonverbal synchronization in motion energy analysis time-series.\n\nThe goal of rMEA is to provide a suite of tools useful to read, visualize and export bivariate Motion Energy time-series. Lagged synchrony between subjects can be analyzed through windowed cross-correlation. Surrogate data generation allows an estimation of pseudosynchrony that helps to estimate the effect size of the observed synchronization.", "[]", "[{'term': 'Imaging', 'uri': 'http://edamontology.org/topic_3382'}, {'term': 'Gene expression', 'uri': 'http://edamontology.org/topic_0203'}, {'term': 'Literature and language', 'uri': 'http://edamontology.org/topic_3068'}]", "[]", "[]"], ["breedbase", "Breedbase is a comprehensive breeding management and analysis software. It can be used to design field layouts, collect phenotypic information using tablets, support the collection of genotyping samples in a field, store large amounts of high density genotypic information, and provide Genomic Selection related analyses and predictions. Breedbase supports the BrAPI standard.", "['Bioinformatics portal']", "[{'term': 'Agricultural science', 'uri': 'http://edamontology.org/topic_3810'}, {'term': 'Plant biology', 'uri': 'http://edamontology.org/topic_0780'}, {'term': 'Genotype and phenotype', 'uri': 'http://edamontology.org/topic_0625'}, {'term': 'NMR', 'uri': 'http://edamontology.org/topic_0593'}, {'term': 'Workflows', 'uri': 'http://edamontology.org/topic_0769'}]", "[]", "[]"], ["reactioncode", "Format for Reaction Searching, Analysis, Classification, Transform, and Encoding/Decoding.\n\nReactionCode is a new versatile format for searching, analysis, classification, transform, and encoding decoding of reactions.", "[]", "[{'term': 'Machine learning', 'uri': 'http://edamontology.org/topic_3474'}, {'term': 'Chemistry', 'uri': 'http://edamontology.org/topic_3314'}, {'term': 'Molecular biology', 'uri': 'http://edamontology.org/topic_3047'}, {'term': 'Small molecules', 'uri': 'http://edamontology.org/topic_0154'}]", "[]", "[]"], ["rawr", "Direct access to raw mass spectrometry data in R.\n\nR interface for Thermo Fisher Scientifc raw files branched from rawDiag. This package wraps the functionality of the RawFileReader .NET assembly. Within the R environment spectra and chromatograms are represented by S3 objects. All objects are currently kept in memory. Later versions will support on-disc backend processing and lazy evaluation.\n\nPlease install the latest release from https://github.com/fgcz/rawR/releases according to the provided instructions.", "[]", "[{'term': 'Proteomics experiment', 'uri': 'http://edamontology.org/topic_3520'}, {'term': 'Proteomics', 'uri': 'http://edamontology.org/topic_0121'}, {'term': 'Sequence assembly', 'uri': 'http://edamontology.org/topic_0196'}]", "[]", "[]"]]};
        dt_args = eval_functions(dt_args);
        table = $('#60b6c368-6578-4177-a8e0-0300b711eef6').DataTable(dt_args);
    });
})
</script>
</div>


