<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Painel Elétrico ETA & Assistente WhatsApp</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Font Awesome para ícones -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Fonte Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6;
        }
        /* Padrão sutil de fundo estilo WhatsApp Web */
        .whatsapp-bg {
            background-color: #EFEAE2;
            background-image: radial-gradient(#d5cec2 1px, transparent 1px), radial-gradient(#d5cec2 1px, #EFEAE2 1px);
            background-size: 40px 40px;
            background-position: 0 0, 20px 20px;
        }
        /* Barra de rolagem personalizada */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(0, 0, 0, 0.2);
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(0, 0, 0, 0.35);
        }
        /* Efeito de rabicho nos balões do WhatsApp */
        .bubble-bot::before {
            content: "";
            position: absolute;
            top: 0;
            left: -8px;
            width: 0;
            height: 0;
            border-top: 8px solid #FFFFFF;
            border-left: 8px solid transparent;
        }
        .bubble-user::before {
            content: "";
            position: absolute;
            top: 0;
            right: -8px;
            width: 0;
            height: 0;
            border-top: 8px solid #D9FDD3;
            border-right: 8px solid transparent;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .msg-animate {
            animation: fadeIn 0.22s ease-out forwards;
        }
    </style>
</head>
<body class="text-slate-800 antialiased selection:bg-emerald-200 selection:text-emerald-900">

    <!-- Barra Superior -->
    <header class="bg-slate-900 text-white shadow-md sticky top-0 z-30">
        <div class="max-w-[1600px] mx-auto px-4 sm:px-6 py-3 flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <div class="bg-emerald-500/20 border border-emerald-400/30 p-2 rounded-xl text-emerald-400">
                    <i class="fa-solid fa-bolt-lightning text-xl"></i>
                </div>
                <div>
                    <h1 class="text-base sm:text-lg font-bold tracking-tight leading-tight">Painel Elétrico & Automação — ETA</h1>
                    <p class="text-xs text-slate-400">Base de Dados: <code class="text-emerald-300">especificacao_painel_eta.csv</code></p>
                </div>
            </div>

            <div class="flex items-center gap-2">
                <button onclick="openPythonModal()" class="flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-medium transition shadow-sm">
                    <i class="fa-brands fa-python text-amber-400 text-base"></i>
                    <span>Código Python / Streamlit</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Layout Principal Dividido: Dashboard (Esquerda) + Chat WhatsApp (Direita) -->
    <main class="max-w-[1600px] mx-auto p-3 sm:p-5 grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
        
        <!-- COLUNA ESQUERDA: GRÁFICO E DADOS DO CSV (7 colunas no desktop) -->
        <section class="lg:col-span-7 flex flex-col gap-5">
            
            <!-- KPIs Rápidos -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div id="card-compacta" class="bg-white rounded-2xl p-4 shadow-sm border border-slate-200/80 transition-all duration-300">
                    <div class="flex items-center justify-between mb-1">
                        <span class="text-xs font-semibold uppercase tracking-wider text-sky-600 bg-sky-50 px-2.5 py-0.5 rounded-full">Pequeno Porte (até 20 m³/h)</span>
                        <i class="fa-solid fa-water text-sky-500"></i>
                    </div>
                    <h2 class="text-sm text-slate-500 font-medium mt-2">Custo Total Estimado — ETA Compacta</h2>
                    <div class="text-xl sm:text-2xl font-bold text-slate-800 mt-1">R$ 28.000 <span class="text-sm font-normal text-slate-400">a</span> R$ 65.000</div>
                    <p class="text-xs text-slate-500 mt-1.5"><i class="fa-solid fa-circle-info text-sky-500 mr-1"></i>2 a 4 bombas, dosadoras simples, CLP + IHM 7"</p>
                </div>

                <div id="card-media" class="bg-white rounded-2xl p-4 shadow-sm border border-slate-200/80 transition-all duration-300">
                    <div class="flex items-center justify-between mb-1">
                        <span class="text-xs font-semibold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded-full">Médio Porte (50 a 200 m³/h)</span>
                        <i class="fa-solid fa-industry text-emerald-600"></i>
                    </div>
                    <h2 class="text-sm text-slate-500 font-medium mt-2">Custo Total Estimado — ETA Industrial</h2>
                    <div class="text-xl sm:text-2xl font-bold text-slate-800 mt-1">R$ 100.000 <span class="text-sm font-normal text-slate-400">a</span> R$ 235.000+</div>
                    <p class="text-xs text-slate-500 mt-1.5"><i class="fa-solid fa-circle-info text-emerald-600 mr-1"></i>Múltiplos inversores, retrolavagem e SCADA</p>
                </div>
            </div>

            <!-- Card do Gráfico Interativo -->
            <div class="bg-white rounded-2xl p-4 sm:p-6 shadow-sm border border-slate-200/80">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4">
                    <div>
                        <h3 id="chart-title" class="text-base sm:text-lg font-bold text-slate-800">Comparativo de Custos Totais (BRL)</h3>
                        <p id="chart-subtitle" class="text-xs text-slate-500">Valores mínimos e máximos estimados por porte de estação</p>
                    </div>
                    
                    <!-- Botões de Alternância de Visualização -->
                    <div class="inline-flex bg-slate-100 p-1 rounded-xl self-start sm:self-auto border border-slate-200/70">
                        <button id="btn-view-totals" onclick="switchChartMode('totals')" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-white text-slate-800 shadow-sm transition">
                            Visão Geral (Totais)
                        </button>
                        <button id="btn-view-details" onclick="switchChartMode('details')" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 hover:text-slate-900 transition">
                            Detalhamento por Item
                        </button>
                    </div>
                </div>

                <!-- Container Responsivo do Canvas -->
                <div class="relative w-full h-[300px] sm:h-[340px]">
                    <canvas id="etaCostChart"></canvas>
                </div>

                <!-- Banner de Destaque Sincronizado com o Chat -->
                <div id="chart-highlight-banner" class="hidden mt-3 bg-emerald-50 border border-emerald-200 text-emerald-900 px-3.5 py-2 rounded-xl text-xs flex items-center justify-between">
                    <span id="chart-highlight-text" class="font-medium"></span>
                    <button onclick="resetChartHighlight()" class="text-emerald-700 hover:text-emerald-950 font-semibold underline ml-3">Limpar filtro</button>
                </div>
            </div>

            <!-- Explorador de Dados do CSV (Abas) -->
            <div class="bg-white rounded-2xl p-4 sm:p-6 shadow-sm border border-slate-200/80">
                <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3 mb-4">
                    <h3 class="text-base font-bold text-slate-800 flex items-center gap-2">
                        <i class="fa-solid fa-table-list text-emerald-600"></i>
                        <span>Especificações Técnicas do CSV</span>
                    </h3>
                    <div class="flex flex-wrap gap-1.5">
                        <button onclick="switchDataTab('custos')" id="tab-custos" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 text-white transition">Custos</button>
                        <button onclick="switchDataTab('montagem')" id="tab-montagem" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 transition">Montagem (5 Etapas)</button>
                        <button onclick="switchDataTab('problemas')" id="tab-problemas" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 transition">Problemas & Prevenção</button>
                    </div>
                </div>

                <!-- Conteúdo Dinâmico das Abas -->
                <div id="data-tab-content" class="overflow-x-auto"></div>
            </div>
        </section>

        <!-- COLUNA DIREITA: CHAT ESTILO WHATSAPP (5 colunas no desktop) -->
        <aside class="lg:col-span-5 lg:sticky lg:top-[72px] flex flex-col bg-white rounded-2xl shadow-md border border-slate-200 overflow-hidden h-[620px] lg:h-[calc(100vh-92px)]">
            
            <!-- Cabeçalho WhatsApp -->
            <div class="bg-[#075E54] text-white px-4 py-3 flex items-center justify-between shadow-sm z-10">
                <div class="flex items-center gap-3">
                    <div class="relative">
                        <div class="w-10 h-10 rounded-full bg-emerald-100 text-[#075E54] flex items-center justify-center font-bold text-lg shadow-inner">
                            <i class="fa-solid fa-robot"></i>
                        </div>
                        <span class="absolute bottom-0 right-0 w-3 h-3 bg-[#25D366] border-2 border-[#075E54] rounded-full"></span>
                    </div>
                    <div>
                        <h2 class="font-semibold text-sm sm:text-base leading-tight">Assistente Técnico ETA</h2>
                        <p class="text-[11px] text-emerald-100/90">online • consulta gráfico e CSV em tempo real</p>
                    </div>
                </div>
                <button onclick="clearChat()" title="Limpar conversa" class="text-emerald-100 hover:text-white p-2 rounded-full hover:bg-white/10 transition">
                    <i class="fa-solid fa-rotate-right text-sm"></i>
                </button>
            </div>

            <!-- Área de Mensagens com fundo WhatsApp -->
            <div id="chat-messages" class="flex-1 whatsapp-bg p-4 overflow-y-auto flex flex-col gap-3">
                <!-- Mensagem inicial inserida via JS -->
            </div>

            <!-- Sugestões Rápidas (Chips) -->
            <div class="bg-[#F0F2F5] px-3 pt-2.5 pb-1.5 border-t border-slate-200/80">
                <p class="text-[10px] font-semibold uppercase tracking-wider text-slate-500 mb-1.5 px-1">Perguntas rápidas:</p>
                <div class="flex gap-1.5 overflow-x-auto pb-1.5 no-scrollbar">
                    <button onclick="sendQuickPrompt('Qual o custo total da ETA Compacta?')" class="shrink-0 bg-white hover:bg-emerald-50 text-slate-700 hover:text-emerald-800 border border-slate-300/80 rounded-full px-3 py-1 text-xs font-medium shadow-xs transition">
                        💰 Custo ETA Compacta
                    </button>
                    <button onclick="sendQuickPrompt('Quanto custa a ETA Médio Porte?')" class="shrink-0 bg-white hover:bg-emerald-50 text-slate-700 hover:text-emerald-800 border border-slate-300/80 rounded-full px-3 py-1 text-xs font-medium shadow-xs transition">
                        🏭 Custo ETA Médio Porte
                    </button>
                    <button onclick="sendQuickPrompt('Quais os problemas de corrosão?')" class="shrink-0 bg-white hover:bg-emerald-50 text-slate-700 hover:text-emerald-800 border border-slate-300/80 rounded-full px-3 py-1 text-xs font-medium shadow-xs transition">
                        🧪 Problemas de corrosão
                    </button>
                    <button onclick="sendQuickPrompt('Quais são as etapas de montagem?')" class="shrink-0 bg-white hover:bg-emerald-50 text-slate-700 hover:text-emerald-800 border border-slate-300/80 rounded-full px-3 py-1 text-xs font-medium shadow-xs transition">
                        🔧 Etapas de montagem
                    </button>
                    <button onclick="sendQuickPrompt('Comparar custos de engenharia e detalhamento')" class="shrink-0 bg-white hover:bg-emerald-50 text-slate-700 hover:text-emerald-800 border border-slate-300/80 rounded-full px-3 py-1 text-xs font-medium shadow-xs transition">
                        📊 Detalhamento por item
                    </button>
                </div>
            </div>

            <!-- Barra de Entrada de Texto WhatsApp -->
            <form id="chat-form" onsubmit="handleUserSubmit(event)" class="bg-[#F0F2F5] px-3 py-2.5 flex items-center gap-2">
                <input 
                    type="text" 
                    id="chat-input" 
                    placeholder="Pergunte sobre custos, etapas, problemas..." 
                    autocomplete="off"
                    class="flex-1 bg-white text-slate-800 placeholder-slate-400 text-sm rounded-full px-4 py-2.5 border border-slate-200 focus:outline-none focus:border-[#00A884] shadow-xs"
                >
                <button 
                    type="submit" 
                    aria-label="Enviar mensagem"
                    class="w-10 h-10 rounded-full bg-[#00A884] hover:bg-[#008f6f] text-white flex items-center justify-center shadow-sm transition shrink-0 cursor-pointer"
                >
                    <i class="fa-solid fa-paper-plane text-sm"></i>
                </button>
            </form>
        </aside>
    </main>

    <!-- MODAL PARA CÓDIGO PYTHON / STREAMLIT -->
    <div id="python-modal" class="fixed inset-0 bg-slate-900/70 backdrop-blur-xs z-50 hidden items-center justify-center p-4">
        <div class="bg-white rounded-2xl max-w-3xl w-full max-h-[88vh] flex flex-col shadow-2xl border border-slate-200 overflow-hidden">
            <div class="px-5 py-4 bg-slate-900 text-white flex items-center justify-between">
                <div class="flex items-center gap-2.5">
                    <i class="fa-brands fa-python text-amber-400 text-xl"></i>
                    <div>
                        <h3 class="font-bold text-sm sm:text-base">Código Python + Streamlit (com Chat estilo WhatsApp)</h3>
                        <p class="text-xs text-slate-400">Execute localmente com: <code class="text-emerald-300">streamlit run app_eta.py</code></p>
                    </div>
                </div>
                <button onclick="closePythonModal()" class="text-slate-400 hover:text-white p-1.5 rounded-lg">
                    <i class="fa-solid fa-xmark text-lg"></i>
                </button>
            </div>
            
            <div class="p-4 bg-slate-50 border-b border-slate-200 flex items-center justify-between gap-2">
                <span class="text-xs text-slate-600">Lê diretamente o arquivo <strong>especificacao_painel_eta.csv</strong> e cria o gráfico + chat lateral.</span>
                <button onclick="copyPythonCode()" id="copy-btn" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold px-3.5 py-2 rounded-xl flex items-center gap-1.5 transition shrink-0">
                    <i class="fa-regular fa-copy"></i>
                    <span>Copiar Código</span>
                </button>
            </div>

            <div class="p-4 overflow-y-auto bg-[#0d1117] text-slate-200 text-xs font-mono leading-relaxed">
<pre id="python-code-block">import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Painel ETA & Chat", layout="wide")

# 1. Carregamento dos dados do CSV
@st.cache_data
def load_data():
    return pd.read_csv("especificacao_painel_eta.csv", sep=";")

df = load_data()

# Estilo WhatsApp customizado via CSS
st.markdown("""
<style>
.wa-header { background-color: #075E54; color: white; padding: 12px 16px; border-radius: 12px 12px 0 0; font-weight: bold; }
.wa-box { background-color: #EFEAE2; padding: 14px; border-radius: 0 0 12px 12px; max-height: 420px; overflow-y: auto; }
.wa-user { background-color: #D9FDD3; color: #111b21; padding: 8px 12px; border-radius: 10px; margin: 6px 0 6px auto; max-width: 82%; text-align: right; }
.wa-bot { background-color: #FFFFFF; color: #111b21; padding: 8px 12px; border-radius: 10px; margin: 6px auto 6px 0; max-width: 85%; box-shadow: 0 1px 1px rgba(0,0,0,0.08); }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Painel Elétrico para Estação de Tratamento de Água (ETA)")

col_graf, col_chat = st.columns([1.4, 1])

with col_graf:
    visao = st.radio("Selecione a visualização:", ["Visão Geral (Totais)", "Detalhamento por Item"], horizontal=True)
    custos_df = df[df["Categoria"] == "Estimativa de Custos"].copy()
    
    if visao == "Visão Geral (Totais)":
        plot_df = custos_df[custos_df["Etapa_ou_Topico"].str.contains("Custo Total Estimado")]
    else:
        plot_df = custos_df[~custos_df["Etapa_ou_Topico"].str.contains("Custo Total Estimado")]

    df_melted = plot_df.melt(
        id_vars=["Etapa_ou_Topico", "Porte_ETA"],
        value_vars=["Custo_Minimo_BRL", "Custo_Maximo_BRL"],
        var_name="Tipo_Custo", value_name="Valor_BRL"
    )
    fig = px.bar(df_melted, x="Etapa_ou_Topico", y="Valor_BRL", color="Tipo_Custo",
                 barmode="group", text_auto=".2s", title="Estimativa de Custos (R$)")
    st.plotly_chart(fig, use_container_width=True)

with col_chat:
    st.markdown('<div class="wa-header">🟢 Assistente Técnico ETA (WhatsApp)</div>', unsafe_allow_html=True)
    if "msgs" not in st.session_state:
        st.session_state.msgs = [("bot", "Olá! Pergunte sobre custos, etapas de montagem ou prevenção de falhas da ETA.")]
    
    pergunta = st.chat_input("Digite sua dúvida sobre o gráfico ou CSV...")
    if pergunta:
        st.session_state.msgs.append(("user", pergunta))
        q = pergunta.lower()
        if "compacta" in q or "pequeno" in q:
            resp = "A ETA Compacta (até 20 m³/h) custa entre R$ 28.000 e R$ 65.000 no total."
        elif "médio" in q or "medio" in q or "industrial" in q:
            resp = "A ETA Médio Porte (50 a 200 m³/h) custa entre R$ 100.000 e R$ 235.000."
        elif "corros" in q or "problema" in q:
            resp = "Principais problemas: Corrosão por cloro, Sobreaquecimento, EMI e Condensação."
        else:
            resp = "Consulte os valores no gráfico ao lado ou pergunte por 'ETA Compacta', 'Médio Porte', 'Montagem' ou 'Corrosão'."
        st.session_state.msgs.append(("bot", resp))

    chat_html = '<div class="wa-box">'
    for role, text in st.session_state.msgs:
        cls = "wa-user" if role == "user" else "wa-bot"
        chat_html += f'<div class="{cls}">{text}</div>'
    chat_html += '</div>'
    st.markdown(chat_html, unsafe_allow_html=True)</pre>
            </div>
        </div>
    </div>

    <script>
        // =========================================================================
        // 1. BASE DE DADOS EXATA DO ARQUIVO especificacao_painel_eta.csv
        // =========================================================================
        const csvData = [
            // Processo de Montagem
            {
                Categoria: "Processo de Montagem",
                Etapa_ou_Topico: "1. Projeto Elétrico e Dimensionamento",
                Descricao_ou_Problema: "Levantamento de cargas (bombas, agitadores, dosadoras, sopradores), definição da arquitetura de automação (CLP, IHM, sensores de pH, turbidez, cloro, nível e vazão) e elaboração de esquemas elétricos e layout.",
                Prevencao_ou_Detalhes: "Normas técnicas aplicáveis e dimensionamento adequado de potência e comando.",
                Porte_ETA: "Todos",
                Custo_Minimo_BRL: null,
                Custo_Maximo_BRL: null
            },
            {
                Categoria: "Processo de Montagem",
                Etapa_ou_Topico: "2. Seleção do Invólucro e Estrutura",
                Descricao_ou_Problema: "Escolha da caixa/painel com grau de proteção IP65 ou IP66 em aço inox 304/316 ou fibra de vidro revestida.",
                Prevencao_ou_Detalhes: "Proteção contra corrosão por umidade e vapores químicos (cloro e sulfato de alumínio).",
                Porte_ETA: "Todos",
                Custo_Minimo_BRL: null,
                Custo_Maximo_BRL: null
            },
            {
                Categoria: "Processo de Montagem",
                Etapa_ou_Topico: "3. Montagem Mecânica",
                Descricao_ou_Problema: "Fixação da placa de montagem interna, trilhos DIN, canaletas de fiação isoladas e elementos de porta (IHM, botoeiras, sinalizadores).",
                Prevencao_ou_Detalhes: "Organização física e isolamento elétrico.",
                Porte_ETA: "Todos",
                Custo_Minimo_BRL: null,
                Custo_Maximo_BRL: null
            },
            {
                Categoria: "Processo de Montagem",
                Etapa_ou_Topico: "4. Montagem Elétrica e Integração",
                Descricao_ou_Problema: "Instalação da seção de potência (disjuntores motor, contatores, inversores, soft-starters) e comando (CLP, I/O 4-20 mA, fontes 24Vdc, relés), anilhamento de cabos e aterramento equipotencial.",
                Prevencao_ou_Detalhes: "Conformidade com NR-10 e NBR 5410.",
                Porte_ETA: "Todos",
                Custo_Minimo_BRL: null,
                Custo_Maximo_BRL: null
            },
            {
                Categoria: "Processo de Montagem",
                Etapa_ou_Topico: "5. Testes de Bancada e Comissionamento",
                Descricao_ou_Problema: "Testes de isolação e continuidade, teste a frio (sem carga) para validar lógicas CLP/IHM e simulação de falhas (trip, falta de fase, nível crítico).",
                Prevencao_ou_Detalhes: "Garantia operacional antes da energização em campo.",
                Porte_ETA: "Todos",
                Custo_Minimo_BRL: null,
                Custo_Maximo_BRL: null
            },
            // Possíveis Problemas
            {
                Categoria: "Possíveis Problemas",
                Etapa_ou_Topico: "Corrosão dos Componentes",
                Descricao_ou_Problema: "Vapores de cloro gasoso, hipoclorito e coagulantes oxidam contatos elétricos, barramentos e placas de CLP.",
                Prevencao_ou_Detalhes: "Prensa-cabos selados, invólucro IP65/IP66 e verniz de proteção (conformal coating).",
                Porte_ETA: "Todos",
                Custo_Minimo_BRL: null,
                Custo_Maximo_BRL: null
            },
            {
                Categoria: "Possíveis Problemas",
                Etapa_ou_Topico: "Sobreaquecimento",
                Descricao_ou_Problema: "Inversores de frequência geram calor contínuo em gabinetes fechados.",
                Prevencao_ou_Detalhes: "Sistemas de exaustão com filtro/grade de vedação ou ar-condicionado.",
                Porte_ETA: "Todos",
                Custo_Minimo_BRL: null,
                Custo_Maximo_BRL: null
            },
            {
                Categoria: "Possíveis Problemas",
                Etapa_ou_Topico: "Ruído e Interferência Eletromagnética (EMI)",
                Descricao_ou_Problema: "Inversores próximos a linhas de sinal sensíveis (pH, turbidez) descalibram leituras.",
                Prevencao_ou_Detalhes: "Separação física de calhas de sinal e potência; cabos blindados com aterramento em ponto único.",
                Porte_ETA: "Todos",
                Custo_Minimo_BRL: null,
                Custo_Maximo_BRL: null
            },
            {
                Categoria: "Possíveis Problemas",
                Etapa_ou_Topico: "Infiltração de Água e Umidade (Condensação)",
                Descricao_ou_Problema: "Mudanças bruscas de temperatura externa geram condensação interna.",
                Prevencao_ou_Detalhes: "Resistências desumidificadoras integradas a termostatos.",
                Porte_ETA: "Todos",
                Custo_Minimo_BRL: null,
                Custo_Maximo_BRL: null
            },
            // Estimativa de Custos - Compacta
            {
                Categoria: "Estimativa de Custos",
                Etapa_ou_Topico: "Componentes elétricos e automação",
                Descricao_ou_Problema: "CLP, IHM 7\", disjuntores, contatores e dosadoras simples.",
                Prevencao_ou_Detalhes: "ETA Compacta",
                Porte_ETA: "Pequeno Porte / Compacta (até 20 m³/h)",
                Custo_Minimo_BRL: 15000,
                Custo_Maximo_BRL: 35000
            },
            {
                Categoria: "Estimativa de Custos",
                Etapa_ou_Topico: "Gabinete Inox/IP66 e montagem",
                Descricao_ou_Problema: "Invólucro protegido e mão de obra de montagem mecânica/elétrica.",
                Prevencao_ou_Detalhes: "ETA Compacta",
                Porte_ETA: "Pequeno Porte / Compacta (até 20 m³/h)",
                Custo_Minimo_BRL: 5000,
                Custo_Maximo_BRL: 12000
            },
            {
                Categoria: "Estimativa de Custos",
                Etapa_ou_Topico: "Engenharia/Programação CLP/IHM",
                Descricao_ou_Problema: "Projeto elétrico, lógica de controle e comissionamento.",
                Prevencao_ou_Detalhes: "ETA Compacta",
                Porte_ETA: "Pequeno Porte / Compacta (até 20 m³/h)",
                Custo_Minimo_BRL: 8000,
                Custo_Maximo_BRL: 18000
            },
            {
                Categoria: "Estimativa de Custos",
                Etapa_ou_Topico: "Custo Total Estimado - ETA Compacta",
                Descricao_ou_Problema: "Soma estimada para painel completo de ETA de pequeno porte.",
                Prevencao_ou_Detalhes: "Valor total de referência.",
                Porte_ETA: "Pequeno Porte / Compacta (até 20 m³/h)",
                Custo_Minimo_BRL: 28000,
                Custo_Maximo_BRL: 65000
            },
            // Estimativa de Custos - Médio Porte
            {
                Categoria: "Estimativa de Custos",
                Etapa_ou_Topico: "Componentes elétricos e automação",
                Descricao_ou_Problema: "Múltiplos inversores, instrumentação avançada e módulos I/O.",
                Prevencao_ou_Detalhes: "ETA Médio Porte",
                Porte_ETA: "Médio Porte / Industrial (50 a 200 m³/h)",
                Custo_Minimo_BRL: 60000,
                Custo_Maximo_BRL: 140000
            },
            {
                Categoria: "Estimativa de Custos",
                Etapa_ou_Topico: "Gabinete Inox e refrigeração",
                Descricao_ou_Problema: "Painel autoportante Inox IP66 com climatização/exaustão.",
                Prevencao_ou_Detalhes: "ETA Médio Porte",
                Porte_ETA: "Médio Porte / Industrial (50 a 200 m³/h)",
                Custo_Minimo_BRL: 15000,
                Custo_Maximo_BRL: 35000
            },
            {
                Categoria: "Estimativa de Custos",
                Etapa_ou_Topico: "Engenharia, testes e programação",
                Descricao_ou_Problema: "Projeto executivo, retrolavagem automática e integração SCADA.",
                Prevencao_ou_Detalhes: "ETA Médio Porte",
                Porte_ETA: "Médio Porte / Industrial (50 a 200 m³/h)",
                Custo_Minimo_BRL: 25000,
                Custo_Maximo_BRL: 60000
            },
            {
                Categoria: "Estimativa de Custos",
                Etapa_ou_Topico: "Custo Total Estimado - ETA Médio Porte",
                Descricao_ou_Problema: "Soma estimada para painel completo de ETA de médio porte/industrial.",
                Prevencao_ou_Detalhes: "Valor total de referência (pode ultrapassar conforme escopo SCADA).",
                Porte_ETA: "Médio Porte / Industrial (50 a 200 m³/h)",
                Custo_Minimo_BRL: 100000,
                Custo_Maximo_BRL: 235000
            }
        ];

        // =========================================================================
        // 2. CONFIGURAÇÃO E CONTROLE DO GRÁFICO (CHART.JS)
        // =========================================================================
        let etaChart = null;
        let currentChartMode = 'totals'; // 'totals' | 'details'

        function formatBRL(val) {
            return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL', maximumFractionDigits: 0 }).format(val);
        }

        function renderChart(mode = 'totals', highlightIndex = null) {
            const ctx = document.getElementById('etaCostChart').getContext('2d');
            if (etaChart) etaChart.destroy();

            let labels = [];
            let minValues = [];
            let maxValues = [];

            if (mode === 'totals') {
                labels = ['ETA Compacta (até 20 m³/h)', 'ETA Médio Porte (50–200 m³/h)'];
                minValues = [28000, 100000];
                maxValues = [65000, 235000];
                document.getElementById('chart-title').textContent = 'Comparativo de Custos Totais (BRL)';
                document.getElementById('chart-subtitle').textContent = 'Soma completa: Componentes + Gabinete + Engenharia';
            } else {
                labels = [
                    'Componentes (Compacta)',
                    'Gabinete/Montagem (Compacta)',
                    'Engenharia/CLP (Compacta)',
                    'Componentes (Médio Porte)',
                    'Gabinete/Refrig. (Médio Porte)',
                    'Engenharia/SCADA (Médio Porte)'
                ];
                minValues = [15000, 5000, 8000, 60000, 15000, 25000];
                maxValues = [35000, 12000, 18000, 140000, 35000, 60000];
                document.getElementById('chart-title').textContent = 'Detalhamento de Custos por Item (BRL)';
                document.getElementById('chart-subtitle').textContent = 'Comparação granular entre ETA Compacta e ETA Médio Porte';
            }

            // Cores com suporte a destaque dinâmico pelo chat
            const minColors = minValues.map((_, i) => {
                if (highlightIndex === null) return 'rgba(14, 165, 233, 0.85)'; // Sky 500
                return (Array.isArray(highlightIndex) ? highlightIndex.includes(i) : highlightIndex === i)
                    ? 'rgba(14, 165, 233, 1)'
                    : 'rgba(14, 165, 233, 0.22)';
            });

            const maxColors = maxValues.map((_, i) => {
                if (highlightIndex === null) return 'rgba(16, 185, 129, 0.88)'; // Emerald 500
                return (Array.isArray(highlightIndex) ? highlightIndex.includes(i) : highlightIndex === i)
                    ? 'rgba(16, 185, 129, 1)'
                    : 'rgba(16, 185, 129, 0.22)';
            });

            etaChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Custo Mínimo (R$)',
                            data: minValues,
                            backgroundColor: minColors,
                            borderColor: 'rgb(2, 132, 199)',
                            borderWidth: 1,
                            borderRadius: 6
                        },
                        {
                            label: 'Custo Máximo (R$)',
                            data: maxValues,
                            backgroundColor: maxColors,
                            borderColor: 'rgb(5, 150, 105)',
                            borderWidth: 1,
                            borderRadius: 6
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    interaction: { mode: 'index', intersect: false },
                    plugins: {
                        legend: {
                            position: 'top',
                            labels: { usePointStyle: true, boxWidth: 8, font: { family: 'Inter', size: 12, weight: '600' } }
                        },
                        tooltip: {
                            backgroundColor: '#0f172a',
                            padding: 12,
                            cornerRadius: 10,
                            callbacks: {
                                label: function(context) {
                                    return ` ${context.dataset.label}: ${formatBRL(context.parsed.y)}`;
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            grid: { color: '#f1f5f9' },
                            ticks: {
                                font: { family: 'Inter', size: 11 },
                                callback: (value) => 'R$ ' + (value / 1000) + 'k'
                            }
                        },
                        x: {
                            grid: { display: false },
                            ticks: { font: { family: 'Inter', size: 11, weight: '500' } }
                        }
                    }
                }
            });
        }

        function switchChartMode(mode, highlightIndex = null, bannerText = null) {
            currentChartMode = mode;
            const btnTotals = document.getElementById('btn-view-totals');
            const btnDetails = document.getElementById('btn-view-details');

            if (mode === 'totals') {
                btnTotals.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-white text-slate-800 shadow-sm transition';
                btnDetails.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 hover:text-slate-900 transition';
            } else {
                btnDetails.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-white text-slate-800 shadow-sm transition';
                btnTotals.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 hover:text-slate-900 transition';
            }

            renderChart(mode, highlightIndex);

            const banner = document.getElementById('chart-highlight-banner');
            if (bannerText) {
                document.getElementById('chart-highlight-text').textContent = bannerText;
                banner.classList.remove('hidden');
            } else {
                banner.classList.add('hidden');
            }
        }

        function resetChartHighlight() {
            document.getElementById('card-compacta').classList.remove('ring-2', 'ring-sky-500');
            document.getElementById('card-media').classList.remove('ring-2', 'ring-emerald-500');
            switchChartMode(currentChartMode, null, null);
        }

        // =========================================================================
        // 3. ABAS DA TABELA DE DADOS DO CSV
        // =========================================================================
        function switchDataTab(tab) {
            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.className = 'tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 transition';
            });
            document.getElementById('tab-' + tab).className = 'tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 text-white transition';

            const container = document.getElementById('data-tab-content');

            if (tab === 'custos') {
                const rows = csvData.filter(d => d.Categoria === 'Estimativa de Custos');
                container.innerHTML = `
                    <table class="w-full text-left border-collapse text-xs sm:text-sm">
                        <thead>
                            <tr class="bg-slate-50 text-slate-600 border-b border-slate-200">
                                <th class="py-2.5 px-3 font-semibold">Item / Etapa</th>
                                <th class="py-2.5 px-3 font-semibold">Porte da ETA</th>
                                <th class="py-2.5 px-3 font-semibold text-right">Mínimo</th>
                                <th class="py-2.5 px-3 font-semibold text-right">Máximo</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100">
                            ${rows.map(r => {
                                const isTotal = r.Etapa_ou_Topico.includes('Total');
                                return `
                                <tr class="${isTotal ? 'bg-emerald-50/70 font-bold text-slate-900' : 'hover:bg-slate-50 text-slate-700'}">
                                    <td class="py-2.5 px-3">${r.Etapa_ou_Topico}</td>
                                    <td class="py-2.5 px-3 text-xs text-slate-500">${r.Porte_ETA}</td>
                                    <td class="py-2.5 px-3 text-right font-mono text-sky-700">${formatBRL(r.Custo_Minimo_BRL)}</td>
                                    <td class="py-2.5 px-3 text-right font-mono text-emerald-700">${formatBRL(r.Custo_Maximo_BRL)}</td>
                                </tr>`;
                            }).join('')}
                        </tbody>
                    </table>`;
            } else if (tab === 'montagem') {
                const rows = csvData.filter(d => d.Categoria === 'Processo de Montagem');
                container.innerHTML = `
                    <div class="space-y-2.5">
                        ${rows.map(r => `
                            <div class="p-3 rounded-xl bg-slate-50 border border-slate-200/70">
                                <div class="font-bold text-slate-800 text-xs sm:text-sm">${r.Etapa_ou_Topico}</div>
                                <p class="text-xs text-slate-600 mt-1 leading-relaxed">${r.Descricao_ou_Problema}</p>
                                <div class="mt-1.5 text-[11px] font-medium text-emerald-700"><i class="fa-solid fa-check-circle mr-1"></i>${r.Prevencao_ou_Detalhes}</div>
                            </div>
                        `).join('')}
                    </div>`;
            } else if (tab === 'problemas') {
                const rows = csvData.filter(d => d.Categoria === 'Possíveis Problemas');
                container.innerHTML = `
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        ${rows.map(r => `
                            <div class="p-3.5 rounded-xl bg-amber-50/50 border border-amber-200/70 flex flex-col justify-between">
                                <div>
                                    <div class="font-bold text-amber-900 text-xs sm:text-sm flex items-center gap-1.5">
                                        <i class="fa-solid fa-triangle-exclamation text-amber-500"></i>
                                        <span>${r.Etapa_ou_Topico}</span>
                                    </div>
                                    <p class="text-xs text-slate-600 mt-1.5">${r.Descricao_ou_Problema}</p>
                                </div>
                                <div class="mt-2.5 pt-2 border-t border-amber-200/50 text-xs text-emerald-800 font-medium">
                                    <strong>Prevenção:</strong> ${r.Prevencao_ou_Detalhes}
                                </div>
                            </div>
                        `).join('')}
                    </div>`;
            }
        }

        // =========================================================================
        // 4. CHAT ESTILO WHATSAPP E MOTOR DE BUSCA NOS DADOS DO GRÁFICO / CSV
        // =========================================================================
        const chatContainer = document.getElementById('chat-messages');

        function getCurrentTime() {
            const now = new Date();
            return now.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
        }

        function appendMessage(sender, htmlText) {
            const wrapper = document.createElement('div');
            wrapper.className = `flex w-full msg-animate ${sender === 'user' ? 'justify-end' : 'justify-start'}`;

            const bubble = document.createElement('div');
            if (sender === 'user') {
                bubble.className = 'relative bubble-user bg-[#D9FDD3] text-[#111b21] rounded-xl rounded-tr-none px-3.5 py-2 max-w-[85%] shadow-xs text-xs sm:text-sm leading-relaxed';
                bubble.innerHTML = `
                    <div>${htmlText}</div>
                    <div class="flex items-center justify-end gap-1 mt-1 text-[10px] text-slate-500">
                        <span>${getCurrentTime()}</span>
                        <i class="fa-solid fa-check-double text-[#53bdeb]"></i>
                    </div>
                `;
            } else {
                bubble.className = 'relative bubble-bot bg-white text-[#111b21] rounded-xl rounded-tl-none px-3.5 py-2.5 max-w-[88%] shadow-xs text-xs sm:text-sm leading-relaxed';
                bubble.innerHTML = `
                    <div>${htmlText}</div>
                    <div class="flex items-center justify-end mt-1 text-[10px] text-slate-400">
                        <span>${getCurrentTime()}</span>
                    </div>
                `;
            }

            wrapper.appendChild(bubble);
            chatContainer.appendChild(wrapper);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        function normalizeText(str) {
            return str.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        }

        // Inteligência de resposta conectada ao gráfico e ao CSV
        function generateBotResponse(rawQuery) {
            const q = normalizeText(rawQuery);

            // Reset de destaques visuais anteriores
            document.getElementById('card-compacta').classList.remove('ring-2', 'ring-sky-500');
            document.getElementById('card-media').classList.remove('ring-2', 'ring-emerald-500');

            // 1. Consulta sobre ETA Compacta / Pequeno Porte
            if (q.includes('compacta') || q.includes('pequeno') || q.includes('20 m3') || q.includes('20m3')) {
                document.getElementById('card-compacta').classList.add('ring-2', 'ring-sky-500');
                switchChartMode('totals', 0, 'Destaque no gráfico: ETA Compacta (R$ 28.000 a R$ 65.000)');
                switchDataTab('custos');
                return `
                    <strong>📊 ETA Compacta / Pequeno Porte (até 20 m³/h)</strong><br>
                    Destaquei essa barra no gráfico ao lado! Veja a composição no CSV:<br><br>
                    • <strong>Componentes elétricos e automação:</strong> R$ 15.000 a R$ 35.000<br>
                    • <strong>Gabinete Inox/IP66 e montagem:</strong> R$ 5.000 a R$ 12.000<br>
                    • <strong>Engenharia / Programação CLP/IHM:</strong> R$ 8.000 a R$ 18.000<br>
                    ✅ <strong>Custo Total Estimado:</strong> <b>R$ 28.000 a R$ 65.000</b>
                `;
            }

            // 2. Consulta sobre ETA Médio Porte / Industrial
            if (q.includes('medio') || q.includes('industrial') || q.includes('50 a 200') || q.includes('200 m3')) {
                document.getElementById('card-media').classList.add('ring-2', 'ring-emerald-500');
                switchChartMode('totals', 1, 'Destaque no gráfico: ETA Médio Porte (R$ 100.000 a R$ 235.000)');
                switchDataTab('custos');
                return `
                    <strong>🏭 ETA Médio Porte / Industrial (50 a 200 m³/h)</strong><br>
                    Destaquei no gráfico ao lado! Os valores estimados são:<br><br>
                    • <strong>Componentes elétricos e automação:</strong> R$ 60.000 a R$ 140.000<br>
                    • <strong>Gabinete Inox e refrigeração:</strong> R$ 15.000 a R$ 35.000<br>
                    • <strong>Engenharia, testes e programação:</strong> R$ 25.000 a R$ 60.000<br>
                    ✅ <strong>Custo Total Estimado:</strong> <b>R$ 100.000 a R$ 235.000+</b><br>
                    <span class="text-xs text-slate-500">*(Pode ultrapassar o máximo conforme escopo SCADA).*</span>
                `;
            }

            // 3. Consulta sobre Engenharia / Programação
            if (q.includes('engenharia') || q.includes('programacao') || q.includes('clp') || q.includes('ihm') || q.includes('scada')) {
                switchChartMode('details', [2, 5], 'Destaque no gráfico: Custos de Engenharia e Programação');
                switchDataTab('custos');
                return `
                    <strong>💻 Comparativo de Engenharia, CLP/IHM e SCADA:</strong><br>
                    Alterei o gráfico para <em>Detalhamento por Item</em> destacando engenharia:<br><br>
                    • <strong>ETA Compacta:</strong> R$ 8.000 a R$ 18.000<br>
                    • <strong>ETA Médio Porte:</strong> R$ 25.000 a R$ 60.000 (inclui retrolavagem automática e integração SCADA)<br>
                    📈 <em>Aumento médio de ~3,2x entre o porte compacto e o industrial.</em>
                `;
            }

            // 4. Consulta sobre Gabinete / Invólucro / IP65 / IP66 / Inox
            if (q.includes('gabinete') || q.includes('involucro') || q.includes('inox') || q.includes('ip65') || q.includes('ip66')) {
                switchChartMode('details', [1, 4], 'Destaque no gráfico: Custos de Gabinete Inox e Montagem/Refrigeração');
                switchDataTab('custos');
                return `
                    <strong>🛡️ Gabinete e Invólucro (IP65 / IP66 em Aço Inox 304/316):</strong><br>
                    • <strong>ETA Compacta (Gabinete + montagem):</strong> R$ 5.000 a R$ 12.000<br>
                    • <strong>ETA Médio Porte (Gabinete + refrigeração):</strong> R$ 15.000 a R$ 35.000<br><br>
                    💡 <em>Nota técnica:</em> Utiliza-se aço inox 304/316 ou fibra de vidro revestida para resistir à umidade e vapores de cloro/sulfato de alumínio.
                `;
            }

            // 5. Consulta sobre Componentes Elétricos
            if (q.includes('componente') || q.includes('inversor') || q.includes('disjuntor') || q.includes('contator')) {
                switchChartMode('details', [0, 3], 'Destaque no gráfico: Componentes Elétricos e Automação');
                switchDataTab('custos');
                return `
                    <strong>⚡ Componentes Elétricos e Automação:</strong><br>
                    Representam cerca de <strong>54% a 60%</strong> do custo total do painel:<br><br>
                    • <strong>ETA Compacta:</strong> R$ 15.000 a R$ 35.000<br>
                    • <strong>ETA Médio Porte:</strong> R$ 60.000 a R$ 140.000
                `;
            }

            // 6. Consulta sobre Detalhamento / Comparação Geral
            if (q.includes('detalhamento') || q.includes('comparar') || q.includes('diferenca') || q.includes('grafico')) {
                switchChartMode('details', null, 'Visualização alterada para Detalhamento por Item');
                return `
                    <strong>📊 Visão Detalhada Ativada no Gráfico!</strong><br>
                    Agora você pode comparar lado a lado os 3 pilares de custo:<br>
                    1. <strong>Componentes:</strong> R$ 15k–35k (Compacta) vs R$ 60k–140k (Média)<br>
                    2. <strong>Gabinete:</strong> R$ 5k–12k (Compacta) vs R$ 15k–35k (Média)<br>
                    3. <strong>Engenharia:</strong> R$ 8k–18k (Compacta) vs R$ 25k–60k (Média)<br><br>
                    A ETA Médio Porte custa em média <strong>3,6x mais</strong> que a Compacta.
                `;
            }

            // 7. Consulta sobre Problemas / Corrosão / Sobreaquecimento / EMI / Umidade
            if (q.includes('problema') || q.includes('corros') || q.includes('aquec') || q.includes('ruido') || q.includes('emi') || q.includes('umidade') || q.includes('condens') || q.includes('prevencao')) {
                switchDataTab('problemas');
                if (q.includes('corros')) {
                    return `
                        <strong>🧪 Problema: Corrosão dos Componentes</strong><br>
                        • <strong>Causa:</strong> Vapores de cloro gasoso, hipoclorito e coagulantes oxidam contatos elétricos, barramentos e placas de CLP.<br>
                        • <strong>Prevenção:</strong> Usar prensa-cabos selados, invólucro IP65/IP66 e aplicar verniz protetor (<em>conformal coating</em>) nas placas.
                    `;
                }
                return `
                    <strong>⚠️ 4 Principais Problemas e Prevenções (Aba atualizada):</strong><br><br>
                    1. <strong>Corrosão:</strong> Prensa-cabos selados, IP65/IP66 e verniz <em>conformal coating</em>.<br>
                    2. <strong>Sobreaquecimento:</strong> Exaustão com filtro/vedação ou ar-condicionado para painéis.<br>
                    3. <strong>Ruído / EMI:</strong> Separar calhas de sinal (4-20 mA) e potência; cabos blindados aterrados em ponto único.<br>
                    4. <strong>Umidade / Condensação:</strong> Resistências desumidificadoras com termostato.
                `;
            }

            // 8. Consulta sobre Etapas de Montagem / Normas
            if (q.includes('etapa') || q.includes('montagem') || q.includes('passo') || q.includes('nr-10') || q.includes('nr10') || q.includes('5410') || q.includes('teste')) {
                switchDataTab('montagem');
                return `
                    <strong>🔧 5 Etapas do Processo de Montagem (Aba atualizada):</strong><br><br>
                    1️⃣ <strong>Projeto Elétrico:</strong> Levantamento de cargas, arquitetura CLP/IHM e diagramas.<br>
                    2️⃣ <strong>Invólucro:</strong> Caixa IP65/IP66 em Inox 304/316 ou fibra revestida.<br>
                    3️⃣ <strong>Montagem Mecânica:</strong> Placa interna, trilhos DIN, canaletas e elementos de porta.<br>
                    4️⃣ <strong>Montagem Elétrica:</strong> Potência, comando 24Vdc, anilhamento e aterramento (<strong>NR-10 e NBR 5410</strong>).<br>
                    5️⃣ <strong>Testes e Comissionamento:</strong> Isolação, continuidade, teste a frio e simulação de falhas.
                `;
            }

            // 9. Resposta padrão orientativa
            return `
                Não encontrei um termo exato para "<em>${rawQuery}</em>", mas posso consultar qualquer dado do gráfico e do CSV!<br><br>
                Experimente perguntar sobre:<br>
                • <strong>"Custo total da ETA Compacta"</strong> ou <strong>"ETA Médio Porte"</strong><br>
                • <strong>"Detalhamento por item"</strong> ou <strong>"Custos de engenharia"</strong><br>
                • <strong>"Etapas de montagem"</strong> ou <strong>"Normas NR-10"</strong><br>
                • <strong>"Problemas de corrosão"</strong> ou <strong>"Prevenção de umidade"</strong>
            `;
        }

        function handleUserSubmit(event) {
            event.preventDefault();
            const input = document.getElementById('chat-input');
            const text = input.value.trim();
            if (!text) return;

            appendMessage('user', text);
            input.value = '';

            setTimeout(() => {
                const reply = generateBotResponse(text);
                appendMessage('bot', reply);
            }, 300);
        }

        function sendQuickPrompt(text) {
            appendMessage('user', text);
            setTimeout(() => {
                const reply = generateBotResponse(text);
                appendMessage('bot', reply);
            }, 250);
        }

        function clearChat() {
            chatContainer.innerHTML = '';
            resetChartHighlight();
            initChat();
        }

        function initChat() {
            appendMessage('bot', `
                Olá! 👋 Sou o assistente técnico do painel da <strong>Estação de Tratamento de Água (ETA)</strong>.<br><br>
                Estou conectado diretamente ao gráfico e ao arquivo <code>especificacao_painel_eta.csv</code>. Pergunte sobre <strong>valores mínimos/máximos, etapas de montagem ou prevenção de falhas</strong> que eu respondo e destaco no gráfico para você!
            `);
        }

        // =========================================================================
        // 5. CONTROLE DO MODAL DE CÓDIGO PYTHON / STREAMLIT
        // =========================================================================
        function openPythonModal() {
            const modal = document.getElementById('python-modal');
            modal.classList.remove('hidden');
            modal.classList.add('flex');
        }

        function closePythonModal() {
            const modal = document.getElementById('python-modal');
            modal.classList.add('hidden');
            modal.classList.remove('flex');
        }

        function copyPythonCode() {
            const codeText = document.getElementById('python-code-block').innerText;
            const textarea = document.createElement('textarea');
            textarea.value = codeText;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);

            const btn = document.getElementById('copy-btn');
            btn.innerHTML = '<i class="fa-solid fa-check"></i><span>Copiado!</span>';
            setTimeout(() => {
                btn.innerHTML = '<i class="fa-regular fa-copy"></i><span>Copiar Código</span>';
            }, 2000);
        }

        // Inicialização ao carregar a página
        window.onload = function() {
            renderChart('totals');
            switchDataTab('custos');
            initChat();
        };
    </script>
</body>
</html>
