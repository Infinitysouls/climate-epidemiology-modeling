# Ethics Guidelines

## Purpose

This toolkit is designed for legitimate public health research and epidemiological studies. Users must adhere to ethical guidelines when using this software and any resulting data.

## Core Principles

### 1. Research Integrity

Use this toolkit only for activities that contribute to:
- Epidemiological research
- Health surveillance and early warning
- Public health planning and response
- Academic research and education

### 2. Data Privacy

When working with health data:

- **Aggregate Data Only**: Work with location-level data, not individual case information
- **Minimum Population**: Report findings only for populations of 5+ individuals
- **Geographic Generalization**: Consider reporting at district/state level rather than exact coordinates
- **De-identification**: Remove any personally identifiable information before analysis

### 3. Data Attribution

Always attribute data sources:

- **Climate Data**: Cite the satellite-based climate data source in publications
- **Health Data**: Acknowledge the source of surveillance data

### 4. Responsible Reporting

When publishing findings:

- Contextualize results within limitations
- Avoid stigmatizing communities or regions
- Present findings in ways that support public health action
- Disclose any conflicts of interest

## Data Handling Best Practices

### Input Data

| Data Type | Recommended Handling |
|-----------|---------------------|
| Location coordinates | Aggregate to district level when possible |
| Event dates | Use for temporal analysis, not individual tracking |
| Case counts | Aggregate, never report single-case data |
| Population data | Use official census or estimate sources |

### Output Data

- Review all generated datasets for privacy concerns before sharing
- Apply k-anonymity (minimum 5 records per group)
- Consider adding noise to exact coordinates

## Legal Compliance

Users are responsible for:

1. **Local Laws**: Comply with data protection regulations in their jurisdiction
   - GDPR (European Union)
   - HIPAA (United States)
   - Other applicable laws

2. **Data Sharing Agreements**: Honor any terms under which data was obtained

3. **Institutional Requirements**: Obtain necessary ethics approvals (IRB, IEC) for research projects

## Prohibited Uses

This toolkit must NOT be used for:

- Targeting specific individuals or households
- Insurance or employment decisions
- Any form of surveillance beyond public health purposes
- Activities that could harm public health efforts

## Disclaimer

The authors of this toolkit provide it "as is" without warranty. Users assume all responsibility for:
- Appropriate use of the software
- Interpretation of results
- Compliance with applicable laws and regulations

## Reporting Concerns

If you identify ethical concerns or misuse:
- Open an issue on GitHub
- Contact your institutional ethics board
- Report to relevant public health authorities

## Citation and Attribution

When using this toolkit in research, cite:

```
Epidemiological Climate Toolkit
https://github.com/Infinitysouls/epidemiological-climate-toolkit
```

## Acknowledgments

This toolkit was developed for public health research purposes and draws on:
- Open climate data from satellite sources
- Public health surveillance infrastructure
- Open source software principles

## Contact

For questions about appropriate use, please open an issue on GitHub.

---

*Last updated: 2024*
