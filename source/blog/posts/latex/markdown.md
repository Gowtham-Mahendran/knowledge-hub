---
title: "Latex"
date: 2025-12-22
description: "Notes on optimizing background tasks for Python Course Platform"
categories: [Linux]
tags: [latex, django, performance]
draft: true
---

In vscodium, go to file > preferences > settings > word wrap (ON)
this will wrap long lines  <!-- more -->

1. Name the file as `main.tex`

2. give a class to the document

```tex
\documentclass{article}
```

3. A document can be started and ended with

```tex
\begin{document}

\end{document}

```

4. Set the margins using

```tex
\usepackage{geometry}   #import a package
\geometry{margin=1in}   #use the package to set
```

5. Sections

```tex
\section{Title}
\subsection{Sub}
\subsubsection{Subsub}
```

6. Bold, italic and code

```tex
\textbf{bold}
\textit{italic}
```
7. Coding

```tex
\usepackage{listings}
\begin{lstlisting}[language=Python]
\end{lstlisting}
```

8. Images

```tex
\usepackage{float}          #Use [H] (forces exact placement)
\usepackage{graphicx}

\begin{figure}[H]           #Try to place this figure **here**
\centering
\includegraphics[width=0.6\textwidth]{images/plot.png}
\caption{Example}
\end{figure}
```

9. other file

```tex
\usepackage[utf8]{inputenc}
\input{intro/intro}
```

When using another `intro.tex` file, here are the things to remember:
    1. All the packages must be in `main.tex` file
    2. The `intro.tex` file should not have `\begin{document}` or `\end{document}`
    3. All the image paths are relative to the `main.tex` file
    4. It should only have the content

10. Making bullet points
```tex
\begin{itemize}
  \item First point
  \item Second point
  \item Third point
\end{itemize}
```
```tex
\begin{enumerate}
  \item First
  \item Second
\end{enumerate}
```

11. superscript and subscript

```tex
text$^{sup}$
text$_{sub}$
```

12. Equation

```tex
\begin{equation}
a = b + c
\end{equation}


\begin{equation}
    X_L = 2\pi f L
\end{equation}
```