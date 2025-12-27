---
title: "LaTeX Quick Notes"
date: 2025-12-27
description: "A minimal, practical guide to writing clean LaTeX documents"
categories: [Linux]
tags: [latex, productivity]
draft: False
---

Here you can find a minimal starting guide to work on latex. Some simple syntax for margins, basic text variations, headings, equations, images and tables are included. <!-- more -->

Before starting, enable word wrapping in **VSCodium**:

**File → Preferences → Settings → Word Wrap → ON**

This makes LaTeX source files far easier to read and maintain.

---

## 1. Start with a main file

Always create a central entry point:

```tex
main.tex
```

This file defines the document layout and imports all other content.

---

## 2. Define the document class

Every LaTeX document starts with a class:

```tex
\documentclass{article}
```
!!! info "LaTeX document classes"
    **article** → Articles in scientific journals, short reports, and other short documents<br>
    **proc** → Proceedings class based on the `article` class<br>
    **report** → Longer reports with chapters, small books, PhD theses<br>
    **book** → Full-length books<br>
    **beamer** → Presentations and slides<br>
    **letter** → Letters and formal correspondence<br>

---

## 3. Document boundaries

All content must live inside:

```tex
\begin{document}

\end{document}
```

---

## 4. Set page margins

Use the `geometry` package for predictable layouts:

```tex
\usepackage{geometry}
\geometry{margin=1in}
```

---

## 5. Sections and hierarchy

```tex
\section{Title}
\subsection{Subsection}
\subsubsection{Subsubsection}
```

---

## 6. Text formatting

```tex
\textbf{bold}
\textit{italic}
```

---

## 7. Code listings

```tex
\usepackage{listings}

\begin{lstlisting}[language=Python]
print("Hello, LaTeX")
\end{lstlisting}
```

---

## 8. Figures and images

```tex
\usepackage{float}
\usepackage{graphicx}

\begin{figure}[H]
\centering
\includegraphics[width=0.6\textwidth]{images/plot.png}
\caption{Example}
\end{figure}
```

* `[H]` forces exact placement
* Image paths are always relative to `main.tex`

---

## 9. Splitting content into files

```tex
\usepackage[utf8]{inputenc}
\input{intro/intro}
```

When using secondary files like `intro.tex`, follow these rules:

1. All packages belong in `main.tex`
2. Do **not** use `\begin{document}` or `\end{document}`
3. Image paths stay relative to `main.tex`
4. Only content goes into sub-files

---

## 10. Lists

### Bullet points

```tex
\begin{itemize}
  \item First point
  \item Second point
  \item Third point
\end{itemize}
```

### Numbered lists

```tex
\begin{enumerate}
  \item First
  \item Second
\end{enumerate}
```

---

## 11. Superscripts and subscripts

```tex
text$^{sup}$
text$_{sub}$
```

---

## 12. Equations

```tex
\begin{equation}
a = b + c
\end{equation}

\begin{equation}
X_L = 2\pi f L
\end{equation}
```

---

## 13. Tables

```tex
\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{lll}
\hline
\textbf{Parameter} & \textbf{Definition} & \textbf{Value} \\
\hline
x & y & z \\
u & v & w \\
\hline
\multicolumn{3}{c}{\textbf{Name}} \\
\hline
a & b & c \\
\hline
\end{tabular}
\caption{Caption goes here}
\end{table}
```

---

This setup is intentionally simple. It keeps LaTeX predictable, readable, and maintainable—even as documents grow large.
