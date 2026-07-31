# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_x0ETRmd6GgXY` — Micro-Niche Adaptive Forecasting for Short Time Series
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-31 01:25:35 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: Micro-Niche Adaptive Forecasting for Short Time Series
abstract: >-
  Forecasting very short time series presents a significant challenge for traditional and even many adaptive models due to
  data scarcity and the inability to learn complex parameters or stable regimes. Inspired by the ecological principle of niche
  partitioning, we propose Micro-Niche Adaptive Forecasting, a novel approach that dynamically selects between simple forecasting
  models (e.g., 3-point moving average, naive last-value forecast) based on instantly computable local 'micro-environmental
  cues' such as trend direction and recent volatility. Our experimental evaluation on a diverse set of synthetic short time
  series demonstrates that this adaptive strategy consistently outperforms both individual baseline models, achieving a 48.3%
  lower Mean Squared Error (MSE) than the naive forecast and a 66.5% lower MSE than the 3-point moving average. This work
  highlights the effectiveness of agile, context-aware model selection for enhancing predictive accuracy in data-constrained
  scenarios.
paper_text: |
  # Introduction

  Accurate time series forecasting is critical across numerous domains, from financial markets to environmental monitoring. However, many real-world applications contend with extremely short time series, where traditional forecasting methods, often reliant on substantial historical data for parameter learning or robust regime identification, falter [1, 2]. The challenge is particularly acute in dynamic environments where underlying data patterns can shift rapidly, invalidating static models and demanding immediate adaptability from minimal observations. Existing adaptive ensemble methods and regime-switching models typically require more data to learn complex weights or transition probabilities, limiting their efficacy in these data-scarce scenarios [3, 4].

  To address this critical gap, we introduce **Micro-Niche Adaptive Forecasting**, a novel paradigm inspired by the ecological principle of niche partitioning. In biological ecosystems, diverse species coexist by specializing in distinct 'niches'—specific environmental conditions where they are optimally adapted. Transposing this concept to forecasting, we hypothesize that simple forecasting models, each possessing inherent strengths under particular data characteristics, can collectively achieve superior performance by dynamically specializing in their optimal 'micro-niches' within a time series. Our approach enables rapid, on-the-fly model selection based on instantly computable local 'micro-environmental cues,' circumventing the data demands of more complex adaptive systems.

  Our method leverages two foundational, computationally inexpensive forecasting models: the 3-point moving average, which provides a smoothing effect, and the naive last-value forecast, which prioritizes immediate responsiveness. We develop a lightweight adaptive mechanism that continuously assesses local data characteristics—such as recent trend (difference between the last two points) and volatility (variance of the last three points)—to determine which of these simple models is momentarily best suited for the next prediction step. This dynamic selection allows each model to operate within its 'optimal micro-niche,' thereby enhancing overall predictive accuracy on very short series.

  We systematically evaluate Micro-Niche Adaptive Forecasting on a diverse collection of short synthetic time series designed to exhibit varied local patterns including trends, oscillations, flatness, and sudden shifts [ARTIFACT:art_9Kdb8LHU-TXq]. Our empirical results demonstrate that the adaptive approach significantly outperforms both standalone simple models across these varied data characteristics. This work presents a computationally efficient and robust solution for short time series forecasting, offering a substantial improvement in predictive performance where data is a limiting factor. Our primary contribution is the demonstration that ecologically-inspired dynamic model selection, even with minimal base models and cues, can effectively address the challenge of small sample sizes.

  [FIGURE:fig1]

  Our key contributions are:
  *   **Novel Micro-Niche Adaptation**: Introduction of a lightweight, ecologically-inspired dynamic selection mechanism that switches between simple forecasting models based on real-time, instantly computable local cues.
  *   **Enhanced Performance on Short Time Series**: Empirical demonstration that Micro-Niche Adaptive Forecasting significantly outperforms both 3-point moving average and naive last-value forecasts on a diverse suite of synthetic short time series.
  *   **Addressing Data Scarcity**: A practical and computationally efficient approach that explicitly targets the limitations of traditional and complex adaptive models in scenarios with very limited data.

  # Related Work

  Traditional time series forecasting, ranging from ARIMA models to more complex deep learning architectures, typically requires substantial historical data to learn stable patterns and parameters. When data is scarce, these methods often struggle with overfitting or insufficient information for robust estimation. The problem is compounded in scenarios where underlying data generating processes exhibit rapid, unpredictable shifts.

  **Adaptive Ensemble Forecasting**. Numerous adaptive ensemble methods exist, aiming to combine multiple forecasting models to achieve superior performance [5, 6]. These often involve sophisticated weighting schemes or meta-learners that adapt model contributions over time (e.g., [7]). However, the learning of these weights or meta-model parameters itself typically demands a non-trivial amount of data, making them less suitable for the extremely short time series considered in our work. Our approach differs by employing a binary, instantly computable switching mechanism between minimal base models, rather than learning complex weighting schemes.

  **Regime-Switching Models**. Regime-switching models (e.g., Markov-switching models) explicitly account for structural breaks and changes in data generating processes by modeling transitions between different regimes, each with its own set of parameters [1]. While powerful, the identification of regimes and the estimation of transition probabilities are data-intensive processes. Research has shown that these models can struggle with small sample sizes, where there is insufficient data to reliably estimate regime parameters or switching dynamics [4]. Our 'micro-niche adaptation' circumvents the need for explicit regime parameter learning, instead relying on immediate local cues to react to instantaneous data characteristics, making it particularly agile in data-scarce environments.

  **Ecological Inspiration**. While the direct application of 'niche partitioning' to dynamic model selection in time series forecasting is novel, the broader concept of drawing inspiration from natural systems for algorithmic design is well-established [8]. Our work specifically transfers the idea of specialized agents thriving in distinct environmental conditions to the realm of simple forecasting models, creating an adaptive system that leverages their individual strengths without complex learning over long horizons.

  # Micro-Niche Adaptive Forecasting

  Our proposed Micro-Niche Adaptive Forecasting approach is designed to overcome the limitations of traditional and complex adaptive forecasting methods when applied to very short time series. The core idea is to dynamically select between simple base models based on real-time 'micro-environmental cues' derived from the most recent data points.

  ## Base Forecasting Models

  We employ two computationally inexpensive and widely understood forecasting models as our base learners:

  1.  **Naive Last-Value Forecast (Naive)**: This model predicts the next value to be identical to the last observed value in the series. It is highly responsive to sudden shifts and performs well in series with persistent values or strong recent trends. Given a time series $y_t$, the forecast $\hat{y}_{t+1}$ is given by $\hat{y}_{t+1} = y_t$.

  2.  **3-Point Moving Average Forecast (MA)**: This model predicts the next value as the average of the last three observed values. It provides a smoothing effect, which can be beneficial in noisy or oscillatory series by reducing the impact of short-term fluctuations. For a time series $y_t$, the forecast $\hat{y}_{t+1}$ is given by $\hat{y}_{t+1} = (y_t + y_{t-1} + y_{t-2}) / 3$.

  In an initial evaluation on a single synthetic sine wave series with noise, the Naive forecast (MSE: 0.128, MAE: 0.311) significantly outperformed the 3-point Moving Average (MSE: 0.361, MAE: 0.531) \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-1560d8-micro-niche-adaptive-forecasting-for-sho/tree/main/round-1/evaluation-1}}. This result underscores that neither simple model is universally superior, motivating the need for an adaptive selection strategy.

  ## Micro-Environmental Cues and Adaptation Logic

  Our adaptive mechanism operates by continuously evaluating local 'micro-environmental cues' to inform the selection of the most appropriate base model for the immediate next prediction. These cues are designed to be instantly computable from very limited recent data, making the approach suitable for short time series.

  We define two primary micro-environmental cues:

  1.  **Local Trend Direction ($\Delta y$)**: Computed as the difference between the last two observed points ($y_t - y_{t-1}$). A positive value indicates an upward trend, a negative value a downward trend, and a value near zero suggests flatness or a turning point.
  2.  **Recent Volatility ($\sigma^2$)**: Computed as the variance of the last three observed points. Higher variance indicates greater fluctuation, while lower variance suggests a more stable segment of the series.

  The adaptive logic determines which model to use based on these cues. While the specific thresholds can be tuned, our implementation \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-1560d8-micro-niche-adaptive-forecasting-for-sho/tree/main/round-2/experiment-1}} employs a heuristic-based switching mechanism. For instance, if the series exhibits a strong, consistent trend (high $\Delta y$) and low volatility, the Naive forecast might be preferred due to its responsiveness. Conversely, in highly volatile or oscillatory segments (high $\sigma^2$ or rapidly changing $\Delta y$), the smoothing property of the 3-point Moving Average might be more advantageous. The decision logic dynamically assigns the prediction based on which model is empirically found to perform better given a combination of these cues within its local 'niche'.

  ## Implementation Details

  The Micro-Niche Adaptive Forecasting algorithm, including the baseline models and the adaptive logic, was implemented in Python . The experimental setup involves processing synthetic time series data, generating predictions for each model (Naive, MA, Adaptive), and calculating Mean Squared Error (MSE) metrics both per series and overall. The output of the experiment includes the original series data, actual values, and predictions from all models, along with detailed MSE results. The algorithm's efficacy is demonstrated by its ability to intelligently partition prediction niches, leading to improved average performance.

  # Experiments and Results

  ## Dataset

  Our evaluation utilized a specially curated dataset of 10 programmatically generated synthetic time series, each with a length between 10 and 20 data points [ARTIFACT:art_9Kdb8LHU-TXq]. This dataset was designed to represent a diverse array of 'micro-environmental cues' and patterns crucial for testing the adaptive model's robustness. The included patterns were:
  *   **Linear Trends**: Upward and downward sloping series.
  *   **Flat Periods**: Segments with minimal change.
  *   **Oscillatory Patterns**: Varying frequencies and amplitudes, including sine waves.
  *   **Sudden Step Changes**: Abrupt shifts in value.
  *   **Shifts in Volatility**: Changes in the degree of data fluctuation.
  *   **Combined Patterns**: Series incorporating multiple pattern types within their short span.

  Each example in the dataset consists of a 3-point input window and the corresponding next value to be predicted, along with metadata detailing the series' origin and pattern type. This controlled diversity ensures a comprehensive evaluation of the micro-niche adaptive strategy across different local data characteristics.

  ## Evaluation Metrics

  To quantify predictive accuracy, we used Mean Squared Error (MSE) and Mean Absolute Error (MAE) as primary evaluation metrics. These metrics provide a robust measure of the difference between predicted and actual values. Lower values for MSE and MAE indicate better forecasting performance.

  $$ MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2 $$
  $$ MAE = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i| $$

  Where $N$ is the number of predictions, $y_i$ is the actual value, and $\hat{y}_i$ is the predicted value.

  ## Results

  The Micro-Niche Adaptive Forecasting approach was evaluated against the Naive Last-Value Forecast and the 3-Point Moving Average Forecast across the diverse synthetic time series dataset \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-1560d8-micro-niche-adaptive-forecasting-for-sho/tree/main/round-2/evaluation-1}}. The aggregate results are summarized in Table 1 and Figure 2.

  [FIGURE:fig2]

  Our experimental results demonstrate that the Micro-Niche Adaptive Forecasting significantly outperforms both baseline models. The adaptive approach achieved an average MSE of **3.903** and an average MAE of **1.875** across all synthetic series. In contrast, the Naive forecast yielded an average MSE of **7.542** and MAE of **2.375**, while the 3-point Moving Average produced an average MSE of **11.653** and MAE of **3.125** .

  This translates to the adaptive model achieving a **48.3% reduction in MSE** compared to the Naive forecast (from 7.542 to 3.903) and an even more substantial **66.5% reduction in MSE** compared to the 3-point Moving Average (from 11.653 to 3.903). Similarly, MAE was reduced by **21.1%** against Naive and **40.0%** against MA.

  The per-series analysis (as observed in the experiment outputs ) further illustrates the adaptive model's effectiveness. For series exhibiting strong linear trends (e.g., `series_1` where input `[10, 8, 6, 4, 2]` output `[4, 2]`), the adaptive model often defaults to the Naive forecast, matching its superior performance (Adaptive MSE = 4.0 vs Naive MSE = 4.0, MA MSE = 16.0). For oscillatory series (e.g., `series_2` where input `[1, 5, 1, 5, 1]` output `[5, 1]`), the adaptive model leverages the smoothing effect of the Moving Average, achieving lower error than the Naive forecast (Adaptive MSE = 7.111 vs Naive MSE = 16.0, MA MSE = 7.111). This dynamic switching based on local cues validates the 'niche partitioning' hypothesis.

  # Discussion

  The results conclusively support our hypothesis: dynamically switching between simple forecasting models based on real-time, instantly computable local 'micro-environmental cues' significantly outperforms either model individually, particularly for short synthetic time series. The Micro-Niche Adaptive Forecasting approach demonstrated a substantial improvement in predictive accuracy as measured by both MSE and MAE across a diverse set of challenging synthetic patterns.

  The observed performance gains can be attributed to the adaptive mechanism's ability to effectively 'partition niches.' When the time series exhibits characteristics where one simple model is inherently superior (e.g., Naive for strong trends, MA for oscillations or noise), the adaptive logic correctly identifies and deploys that model. This avoids the suboptimal performance that would result from using a single static model across all varying local conditions, a limitation highlighted by our initial evaluation showing Naive outperforming MA on a specific sine wave, but not universally .

  This approach directly addresses the challenge of data scarcity in short time series forecasting. Unlike complex adaptive ensembles or regime-switching models that require extensive data for parameter learning, our method relies on minimal, instantaneous cues. This makes it agile and efficient, capable of adapting to rapid changes in underlying data characteristics without the computational overhead or data demands of more sophisticated models.

  **Limitations and Future Work**. While highly effective on synthetic data, the application to real-world short time series (e.g., rapidly changing sensor readings, micro-financial events) will require further validation. The current 'micro-environmental cues' (local trend and volatility) are simple; exploring additional, equally lightweight cues could further refine the adaptive logic. Moreover, the heuristic-based switching mechanism could be augmented with a simple, online learning component (e.g., a reinforcement learning agent) that optimizes switching decisions based on real-time performance feedback, without introducing significant data complexity.

  # Conclusion

  We introduced Micro-Niche Adaptive Forecasting, a novel strategy for improving predictive accuracy in short time series by dynamically selecting between simple forecasting models based on local data characteristics. Inspired by ecological niche partitioning, our method leverages instantly computable micro-environmental cues to allow each model to operate within its optimal 'niche.'

  Our comprehensive evaluation on diverse synthetic time series demonstrated the efficacy of this approach. The Micro-Niche Adaptive Forecast achieved a remarkable 48.3% lower MSE compared to the naive forecast and a 66.5% lower MSE compared to the 3-point moving average. These significant performance gains validate the hypothesis and highlight the potential of agile, context-aware model selection in data-constrained forecasting scenarios.

  This work provides a foundational step towards robust and efficient forecasting for very short, dynamic time series, opening avenues for further research into lightweight adaptive mechanisms and their application to real-world, high-frequency data streams.

  ## Bibliography

  \bibliography{references}
summary: >-
  This paper introduces Micro-Niche Adaptive Forecasting for short time series, dynamically switching between simple models
  (moving average, naive) based on local data cues. Inspired by ecological niche partitioning, the method significantly outperforms
  individual baselines, achieving a 48.3% and 66.5% lower MSE than naive and moving average forecasts, respectively. This
  demonstrates an effective strategy for data-constrained forecasting.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: Micro-Niche Adaptive Forecasting Architecture
caption: >-
  Conceptual architecture of the Micro-Niche Adaptive Forecasting system. Local 'micro-environmental cues' are computed from
  recent time series data, which then inform a dynamic selector to choose between a Naive Forecast and a 3-Point Moving Average
  for the next prediction.
image_gen_detailed_description: >-
  Horizontal flow diagram, left to right. Five labeled boxes: 'Input Time Series (last 3 points)' (light blue rectangle on
  left), 'Compute Micro-Environmental Cues (Local Trend, Volatility)' (green square), 'Dynamic Model Selector' (yellow diamond,
  decision point), 'Naive Last-Value Forecast' (dark blue rectangle), '3-Point Moving Average Forecast' (dark blue rectangle),
  'Next Predicted Value' (light blue rectangle on right). Arrows: Input to 'Compute Cues'. 'Compute Cues' to 'Dynamic Model
  Selector'. 'Dynamic Model Selector' has two outgoing arrows: one to 'Naive Last-Value Forecast' and one to '3-Point Moving
  Average Forecast'. Both 'Naive Last-Value Forecast' and '3-Point Moving Average Forecast' have arrows merging into 'Next
  Predicted Value'. Use sans-serif font, clean white background, no 3D elements. Aspect ratio 21:9.
aspect_ratio: '21:9'
summary: >-
  Hero architecture diagram explaining the Micro-Niche Adaptive Forecasting process.
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: Comparative Forecasting Performance
caption: >-
  Mean Squared Error (MSE) and Mean Absolute Error (MAE) for Micro-Niche Adaptive Forecasting, Naive Last-Value Forecast,
  and 3-Point Moving Average across diverse synthetic time series. Lower values indicate better performance.
image_gen_detailed_description: >-
  Grouped bar chart comparing three forecasting models: Naive Last-Value Forecast, 3-Point Moving Average, and Micro-Niche
  Adaptive Forecast. X-axis: Model Type. Y-axis: Error Metric Value (ranging from 0 to 15). Two bars per model: one for MSE
  and one for MAE. Data points: Naive MSE = 7.542, Naive MAE = 2.375; MA MSE = 11.653, MA MAE = 3.125; Adaptive MSE = 3.903,
  Adaptive MAE = 1.875. Use distinct colors for each model type. Sans-serif font, white background. Aspect ratio 16:9.
aspect_ratio: '21:9'
summary: >-
  Compares MSE and MAE of adaptive model vs. baselines, showing superior performance of the adaptive model.
figure_path: figures/fig2_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-07-31 01:25:35 UTC

```
Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-07-31 01:27:07 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-31 01:27:08 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SYSTEM-USER prompt · 2026-07-31 01:29:40 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/convert_pdf.py"}], "is_error": false, "command": "create", "path": "/ai-inventor/aii_da
  - [agent_think]: Okay, here's my interpretation of that simple instruction, delivered as a stream of thought:

**Executing the Script**

Alright, that's straightforward enough. The immediate next step is to run the Python script. No real ambiguity there. The instruction *is* the action. There's no higher-level strat
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "python3 /ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/convert_pdf.py",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Saved /ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_1.png\nSaved /ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/w
  - [agent_think]: Here's my thought process, as it stands:

**Visual Review Strategy for PDF Conversion**

Okay, so the PDF is now split into 7 PNG images. My plan, as directed by the instructions and the `aii-image-gen` tool (and corrected understanding of the `aii-paper-to-latex` and `aii-web-tools` as well), is to
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_1.png",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_2.png",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_3.png",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_4.png",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_5.png",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_6.png",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_7.png",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Image file /ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_1.png read successfully. Displaying image content."}, {"cache_prompt": false, "type": "imag
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Image file /ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_2.png read successfully. Displaying image content."}, {"cache_prompt": false, "type": "imag
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Image file /ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_3.png read successfully. Displaying image content."}, {"cache_prompt": false, "type": "imag
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Image file /ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_4.png read successfully. Displaying image content."}, {"cache_prompt": false, "type": "imag
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Image file /ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_5.png read successfully. Displaying image content."}, {"cache_prompt": false, "type": "imag
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Image file /ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_6.png read successfully. Displaying image content."}, {"cache_prompt": false, "type": "imag
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Image file /ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages/page_7.png read successfully. Displaying image content."}, {"cache_prompt": false, "type": "imag
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: Micro-Niche Adaptive Forecasting for Short Time Series
abstract: >-
  Forecasting very short time series presents a significant challenge for traditional and even many adaptive models due to
  data scarcity and the inability to learn complex parameters or stable regimes. Inspired by the ecological principle of niche
  partitioning, we propose Micro-Niche Adaptive Forecasting, a novel approach that dynamically selects between simple forecasting
  models (e.g., 3-point moving average, naive last-value forecast) based on instantly computable local 'micro-environmental
  cues' such as trend direction and recent volatility. Our experimental evaluation on a diverse set of synthetic short time
  series demonstrates that this adaptive strategy consistently outperforms both individual baseline models, achieving a 48.3%
  lower Mean Squared Error (MSE) than the naive forecast and a 66.5% lower MSE than the 3-point moving average. This work
  highlights the effectiveness of agile, context-aware model selection for enhancing predictive accuracy in data-constrained
  scenarios.
paper_text: |
  # Introduction

  Accurate time series forecasting is critical across numerous domains, from financial markets to environmental monitoring. However, many real-world applications contend with extremely short time series, where traditional forecasting methods, often reliant on substantial historical data for parameter learning or robust regime identification, falter [1, 2]. The challenge is particularly acute in dynamic environments where underlying data patterns can shift rapidly, invalidating static models and demanding immediate adaptability from minimal observations. Existing adaptive ensemble methods and regime-switching models typically require more data to learn complex weights or transition probabilities, limiting their efficacy in these data-scarce scenarios [3, 4].

  To address this critical gap, we introduce **Micro-Niche Adaptive Forecasting**, a novel paradigm inspired by the ecological principle of niche partitioning. In biological ecosystems, diverse species coexist by specializing in distinct 'niches'—specific environmental conditions where they are optimally adapted. Transposing this concept to forecasting, we hypothesize that simple forecasting models, each possessing inherent strengths under particular data characteristics, can collectively achieve superior performance by dynamically specializing in their optimal 'micro-niches' within a time series. Our approach enables rapid, on-the-fly model selection based on instantly computable local 'micro-environmental cues,' circumventing the data demands of more complex adaptive systems.

  Our method leverages two foundational, computationally inexpensive forecasting models: the 3-point moving average, which provides a smoothing effect, and the naive last-value forecast, which prioritizes immediate responsiveness. We develop a lightweight adaptive mechanism that continuously assesses local data characteristics—such as recent trend (difference between the last two points) and volatility (variance of the last three points)—to determine which of these simple models is momentarily best suited for the next prediction step. This dynamic selection allows each model to operate within its 'optimal micro-niche,' thereby enhancing overall predictive accuracy on very short series.

  We systematically evaluate Micro-Niche Adaptive Forecasting on a diverse collection of short synthetic time series designed to exhibit varied local patterns including trends, oscillations, flatness, and sudden shifts [ARTIFACT:art_9Kdb8LHU-TXq]. Our empirical results demonstrate that the adaptive approach significantly outperforms both standalone simple models across these varied data characteristics. This work presents a computationally efficient and robust solution for short time series forecasting, offering a substantial improvement in predictive performance where data is a limiting factor. Our primary contribution is the demonstration that ecologically-inspired dynamic model selection, even with minimal base models and cues, can effectively address the challenge of small sample sizes.

  [FIGURE:fig1]

  Our key contributions are:
  *   **Novel Micro-Niche Adaptation**: Introduction of a lightweight, ecologically-inspired dynamic selection mechanism that switches between simple forecasting models based on real-time, instantly computable local cues.
  *   **Enhanced Performance on Short Time Series**: Empirical demonstration that Micro-Niche Adaptive Forecasting significantly outperforms both 3-point moving average and naive last-value forecasts on a diverse suite of synthetic short time series.
  *   **Addressing Data Scarcity**: A practical and computationally efficient approach that explicitly targets the limitations of traditional and complex adaptive models in scenarios with very limited data.

  # Related Work

  Traditional time series forecasting, ranging from ARIMA models to more complex deep learning architectures, typically requires substantial historical data to learn stable patterns and parameters. When data is scarce, these methods often struggle with overfitting or insufficient information for robust estimation. The problem is compounded in scenarios where underlying data generating processes exhibit rapid, unpredictable shifts.

  **Adaptive Ensemble Forecasting**. Numerous adaptive ensemble methods exist, aiming to combine multiple forecasting models to achieve superior performance [5, 6]. These often involve sophisticated weighting schemes or meta-learners that adapt model contributions over time (e.g., [7]). However, the learning of these weights or meta-model parameters itself typically demands a non-trivial amount of data, making them less suitable for the extremely short time series considered in our work. Our approach differs by employing a binary, instantly computable switching mechanism between minimal base models, rather than learning complex weighting schemes.

  **Regime-Switching Models**. Regime-switching models (e.g., Markov-switching models) explicitly account for structural breaks and changes in data generating processes by modeling transitions between different regimes, each with its own set of parameters [1]. While powerful, the identification of regimes and the estimation of transition probabilities are data-intensive processes. Research has shown that these models can struggle with small sample sizes, where there is insufficient data to reliably estimate regime parameters or switching dynamics [4]. Our 'micro-niche adaptation' circumvents the need for explicit regime parameter learning, instead relying on immediate local cues to react to instantaneous data characteristics, making it particularly agile in data-scarce environments.

  **Ecological Inspiration**. While the direct application of 'niche partitioning' to dynamic model selection in time series forecasting is novel, the broader concept of drawing inspiration from natural systems for algorithmic design is well-established [8]. Our work specifically transfers the idea of specialized agents thriving in distinct environmental conditions to the realm of simple forecasting models, creating an adaptive system that leverages their individual strengths without complex learning over long horizons.

  # Micro-Niche Adaptive Forecasting

  Our proposed Micro-Niche Adaptive Forecasting approach is designed to overcome the limitations of traditional and complex adaptive forecasting methods when applied to very short time series. The core idea is to dynamically select between simple base models based on real-time 'micro-environmental cues' derived from the most recent data points.

  ## Base Forecasting Models

  We employ two computationally inexpensive and widely understood forecasting models as our base learners:

  1.  **Naive Last-Value Forecast (Naive)**: This model predicts the next value to be identical to the last observed value in the series. It is highly responsive to sudden shifts and performs well in series with persistent values or strong recent trends. Given a time series $y_t$, the forecast $\hat{y}_{t+1}$ is given by $\hat{y}_{t+1} = y_t$.

  2.  **3-Point Moving Average Forecast (MA)**: This model predicts the next value as the average of the last three observed values. It provides a smoothing effect, which can be beneficial in noisy or oscillatory series by reducing the impact of short-term fluctuations. For a time series $y_t$, the forecast $\hat{y}_{t+1}$ is given by $\hat{y}_{t+1} = (y_t + y_{t-1} + y_{t-2}) / 3$.

  In an initial evaluation on a single synthetic sine wave series with noise, the Naive forecast (MSE: 0.128, MAE: 0.311) significantly outperformed the 3-point Moving Average (MSE: 0.361, MAE: 0.531) \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-1560d8-micro-niche-adaptive-forecasting-for-sho/tree/main/round-1/evaluation-1}}. This result underscores that neither simple model is universally superior, motivating the need for an adaptive selection strategy.

  ## Micro-Environmental Cues and Adaptation Logic

  Our adaptive mechanism operates by continuously evaluating local 'micro-environmental cues' to inform the selection of the most appropriate base model for the immediate next prediction. These cues are designed to be instantly computable from very limited recent data, making the approach suitable for short time series.

  We define two primary micro-environmental cues:

  1.  **Local Trend Direction ($\Delta y$)**: Computed as the difference between the last two observed points ($y_t - y_{t-1}$). A positive value indicates an upward trend, a negative value a downward trend, and a value near zero suggests flatness or a turning point.
  2.  **Recent Volatility ($\sigma^2$)**: Computed as the variance of the last three observed points. Higher variance indicates greater fluctuation, while lower variance suggests a more stable segment of the series.

  The adaptive logic determines which model to use based on these cues. While the specific thresholds can be tuned, our implementation \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-1560d8-micro-niche-adaptive-forecasting-for-sho/tree/main/round-2/experiment-1}} employs a heuristic-based switching mechanism. For instance, if the series exhibits a strong, consistent trend (high $\Delta y$) and low volatility, the Naive forecast might be preferred due to its responsiveness. Conversely, in highly volatile or oscillatory segments (high $\sigma^2$ or rapidly changing $\Delta y$), the smoothing property of the 3-point Moving Average might be more advantageous. The decision logic dynamically assigns the prediction based on which model is empirically found to perform better given a combination of these cues within its local 'niche'.

  ## Implementation Details

  The Micro-Niche Adaptive Forecasting algorithm, including the baseline models and the adaptive logic, was implemented in Python . The experimental setup involves processing synthetic time series data, generating predictions for each model (Naive, MA, Adaptive), and calculating Mean Squared Error (MSE) metrics both per series and overall. The output of the experiment includes the original series data, actual values, and predictions from all models, along with detailed MSE results. The algorithm's efficacy is demonstrated by its ability to intelligently partition prediction niches, leading to improved average performance.

  # Experiments and Results

  ## Dataset

  Our evaluation utilized a specially curated dataset of 10 programmatically generated synthetic time series, each with a length between 10 and 20 data points [ARTIFACT:art_9Kdb8LHU-TXq]. This dataset was designed to represent a diverse array of 'micro-environmental cues' and patterns crucial for testing the adaptive model's robustness. The included patterns were:
  *   **Linear Trends**: Upward and downward sloping series.
  *   **Flat Periods**: Segments with minimal change.
  *   **Oscillatory Patterns**: Varying frequencies and amplitudes, including sine waves.
  *   **Sudden Step Changes**: Abrupt shifts in value.
  *   **Shifts in Volatility**: Changes in the degree of data fluctuation.
  *   **Combined Patterns**: Series incorporating multiple pattern types within their short span.

  Each example in the dataset consists of a 3-point input window and the corresponding next value to be predicted, along with metadata detailing the series' origin and pattern type. This controlled diversity ensures a comprehensive evaluation of the micro-niche adaptive strategy across different local data characteristics.

  ## Evaluation Metrics

  To quantify predictive accuracy, we used Mean Squared Error (MSE) and Mean Absolute Error (MAE) as primary evaluation metrics. These metrics provide a robust measure of the difference between predicted and actual values. Lower values for MSE and MAE indicate better forecasting performance.

  $$ MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2 $$
  $$ MAE = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i| $$

  Where $N$ is the number of predictions, $y_i$ is the actual value, and $\hat{y}_i$ is the predicted value.

  ## Results

  The Micro-Niche Adaptive Forecasting approach was evaluated against the Naive Last-Value Forecast and the 3-Point Moving Average Forecast across the diverse synthetic time series dataset \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-1560d8-micro-niche-adaptive-forecasting-for-sho/tree/main/round-2/evaluation-1}}. The aggregate results are summarized in Table 1 and Figure 2.

  [FIGURE:fig2]

  Our experimental results demonstrate that the Micro-Niche Adaptive Forecasting significantly outperforms both baseline models. The adaptive approach achieved an average MSE of **3.903** and an average MAE of **1.875** across all synthetic series. In contrast, the Naive forecast yielded an average MSE of **7.542** and MAE of **2.375**, while the 3-point Moving Average produced an average MSE of **11.653** and MAE of **3.125** .

  This translates to the adaptive model achieving a **48.3% reduction in MSE** compared to the Naive forecast (from 7.542 to 3.903) and an even more substantial **66.5% reduction in MSE** compared to the 3-point Moving Average (from 11.653 to 3.903). Similarly, MAE was reduced by **21.1%** against Naive and **40.0%** against MA.

  The per-series analysis (as observed in the experiment outputs ) further illustrates the adaptive model's effectiveness. For series exhibiting strong linear trends (e.g., `series_1` where input `[10, 8, 6, 4, 2]` output `[4, 2]`), the adaptive model often defaults to the Naive forecast, matching its superior performance (Adaptive MSE = 4.0 vs Naive MSE = 4.0, MA MSE = 16.0). For oscillatory series (e.g., `series_2` where input `[1, 5, 1, 5, 1]` output `[5, 1]`), the adaptive model leverages the smoothing effect of the Moving Average, achieving lower error than the Naive forecast (Adaptive MSE = 7.111 vs Naive MSE = 16.0, MA MSE = 7.111). This dynamic switching based on local cues validates the 'niche partitioning' hypothesis.

  # Discussion

  The results conclusively support our hypothesis: dynamically switching between simple forecasting models based on real-time, instantly computable local 'micro-environmental cues' significantly outperforms either model individually, particularly for short synthetic time series. The Micro-Niche Adaptive Forecasting approach demonstrated a substantial improvement in predictive accuracy as measured by both MSE and MAE across a diverse set of challenging synthetic patterns.

  The observed performance gains can be attributed to the adaptive mechanism's ability to effectively 'partition niches.' When the time series exhibits characteristics where one simple model is inherently superior (e.g., Naive for strong trends, MA for oscillations or noise), the adaptive logic correctly identifies and deploys that model. This avoids the suboptimal performance that would result from using a single static model across all varying local conditions, a limitation highlighted by our initial evaluation showing Naive outperforming MA on a specific sine wave, but not universally .

  This approach directly addresses the challenge of data scarcity in short time series forecasting. Unlike complex adaptive ensembles or regime-switching models that require extensive data for parameter learning, our method relies on minimal, instantaneous cues. This makes it agile and efficient, capable of adapting to rapid changes in underlying data characteristics without the computational overhead or data demands of more sophisticated models.

  **Limitations and Future Work**. While highly effective on synthetic data, the application to real-world short time series (e.g., rapidly changing sensor readings, micro-financial events) will require further validation. The current 'micro-environmental cues' (local trend and volatility) are simple; exploring additional, equally lightweight cues could further refine the adaptive logic. Moreover, the heuristic-based switching mechanism could be augmented with a simple, online learning component (e.g., a reinforcement learning agent) that optimizes switching decisions based on real-time performance feedback, without introducing significant data complexity.

  # Conclusion

  We introduced Micro-Niche Adaptive Forecasting, a novel strategy for improving predictive accuracy in short time series by dynamically selecting between simple forecasting models based on local data characteristics. Inspired by ecological niche partitioning, our method leverages instantly computable micro-environmental cues to allow each model to operate within its optimal 'niche.'

  Our comprehensive evaluation on diverse synthetic time series demonstrated the efficacy of this approach. The Micro-Niche Adaptive Forecast achieved a remarkable 48.3% lower MSE compared to the naive forecast and a 66.5% lower MSE compared to the 3-point moving average. These significant performance gains validate the hypothesis and highlight the potential of agile, context-aware model selection in data-constrained forecasting scenarios.

  This work provides a foundational step towards robust and efficient forecasting for very short, dynamic time series, opening avenues for further research into lightweight adaptive mechanisms and their application to real-world, high-frequency data streams.

  ## Bibliography

  \bibliography{references}
summary: >-
  This paper introduces Micro-Niche Adaptive Forecasting for short time series, dynamically switching between simple models
  (moving average, naive) based on local data cues. Inspired by ecological niche partitioning, the method significantly outperforms
  individual baselines, achieving a 48.3% and 66.5% lower MSE than naive and moving average forecasts, respectively. This
  demonstrates an effective strategy for data-constrained forecasting.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: Micro-Niche Adaptive Forecasting Architecture
caption: >-
  Conceptual architecture of the Micro-Niche Adaptive Forecasting system. Local 'micro-environmental cues' are computed from
  recent time series data, which then inform a dynamic selector to choose between a Naive Forecast and a 3-Point Moving Average
  for the next prediction.
image_gen_detailed_description: >-
  Horizontal flow diagram, left to right. Five labeled boxes: 'Input Time Series (last 3 points)' (light blue rectangle on
  left), 'Compute Micro-Environmental Cues (Local Trend, Volatility)' (green square), 'Dynamic Model Selector' (yellow diamond,
  decision point), 'Naive Last-Value Forecast' (dark blue rectangle), '3-Point Moving Average Forecast' (dark blue rectangle),
  'Next Predicted Value' (light blue rectangle on right). Arrows: Input to 'Compute Cues'. 'Compute Cues' to 'Dynamic Model
  Selector'. 'Dynamic Model Selector' has two outgoing arrows: one to 'Naive Last-Value Forecast' and one to '3-Point Moving
  Average Forecast'. Both 'Naive Last-Value Forecast' and '3-Point Moving Average Forecast' have arrows merging into 'Next
  Predicted Value'. Use sans-serif font, clean white background, no 3D elements. Aspect ratio 21:9.
aspect_ratio: '21:9'
summary: >-
  Hero architecture diagram explaining the Micro-Niche Adaptive Forecasting process.
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: Comparative Forecasting Performance
caption: >-
  Mean Squared Error (MSE) and Mean Absolute Error (MAE) for Micro-Niche Adaptive Forecasting, Naive Last-Value Forecast,
  and 3-Point Moving Average across diverse synthetic time series. Lower values indicate better performance.
image_gen_detailed_description: >-
  Grouped bar chart comparing three forecasting models: Naive Last-Value Forecast, 3-Point Moving Average, and Micro-Niche
  Adaptive Forecast. X-axis: Model Type. Y-axis: Error Metric Value (ranging from 0 to 15). Two bars per model: one for MSE
  and one for MAE. Data points: Naive MSE = 7.542, Naive MAE = 2.375; MA MSE = 11.653, MA MAE = 3.125; Adaptive MSE = 3.903,
  Adaptive MAE = 1.875. Use distinct colors for each model type. Sans-serif font, white background. Aspect ratio 16:9.
aspect_ratio: '21:9'
summary: >-
  Compares MSE and MAE of adaptive model vs. baselines, showing superior performance of the adaptive model.
figure_path: figures/fig2_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [6] HUMAN-USER prompt · 2026-07-31 01:29:40 UTC

```
Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
```

### [7] SYSTEM-USER prompt · 2026-07-31 01:32:06 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `summary`: "Successfully assembled, compiled, and visually reviewed the top-conference LaTeX paper 'Micro-Niche Adaptive Forecasting for Short Time Series' complete with all 2 figures (architecture and performance comparison), full sections (Introduction, Related Work, Method, Experiments, Discussion, Conclusion), BibTeX references, and verified visual formatting." is too short (at least 500 characters, got 354)
Every required field must be present and every field type must match the schema.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
