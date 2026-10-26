insertion_html = """        <!-- CALCULADORA DA LIDA: JANELA DO MANGUE & COMPORTAS DE CARCINICULTURA -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
          
          <!-- CARD 1: JANELA DE TRABALHO NO MANGUE -->
          <div class="bg-gradient-to-br from-amber-500/20 via-mar-950/80 to-mar-900/90 p-5 rounded-2xl border-2 border-amber-400/80 shadow-lg flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs uppercase font-black text-amber-300 flex items-center gap-1.5">
                  <i class="fas fa-stopwatch text-amber-400"></i> Janela no Mangue (Aratu / Caranguejo)
                </span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase bg-emerald-500/20 text-emerald-300 border border-emerald-400/30">
                  Cata no Seco
                </span>
              </div>
              <div class="text-xl sm:text-2xl font-black text-white" id="janela-mangue-horario">
                07:00 às 11:30
              </div>
              <p class="text-xs text-amber-100/90 mt-1.5 leading-relaxed" id="janela-mangue-detalhe">
                Vaza seca a lama a partir das 07h. <strong>Reponta da maré às 12h00</strong>: comece a recolher o material e saia do mangue fundo até 11h30 para não atolar ou ficar ilhado no esteiro.
              </p>
            </div>
            <div class="mt-4 pt-3 border-t border-amber-400/30 flex items-center justify-between text-[11px] text-slate-300">
              <span><i class="fas fa-shoe-prints text-amber-400 mr-1"></i> Terreno Descoberto</span>
              <span class="text-amber-300 font-bold" id="janela-mangue-seguro">Tempo útil: ~4h30</span>
            </div>
          </div>

          <!-- CARD 2: JANELA DE COMPORTAS PARA CARCINICULTURA -->
          <div class="bg-gradient-to-br from-sky-500/20 via-mar-950/80 to-mar-900/90 p-5 rounded-2xl border-2 border-sky-400/80 shadow-lg flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs uppercase font-black text-sky-300 flex items-center gap-1.5">
                  <i class="fas fa-water text-sky-400"></i> Janela de Comportas (Viveiros de Camarão)
                </span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase bg-sky-500/20 text-sky-300 border border-sky-400/30">
                  Cota ≥ 2.2m
                </span>
              </div>
              <div class="text-xl sm:text-2xl font-black text-white" id="janela-comportas-horario">
                15:15 às 17:10
              </div>
              <p class="text-xs text-sky-100/90 mt-1.5 leading-relaxed" id="janela-comportas-detalhe">
                Maré atinge nível de renovação <strong>100% por gravidade</strong> (Pico de 2.4m às 15:58). Economia de bombas e combustível.
              </p>
            </div>
            <div class="mt-4 pt-3 border-t border-sky-400/30 flex items-center justify-between text-[11px] text-slate-300">
              <span><i class="fas fa-shrimp text-sky-400 mr-1"></i> Carcinicultura</span>
              <span class="text-sky-300 font-bold" id="janela-comportas-tempo">Janela: ~2h00 de cota cheia</span>
            </div>
          </div>

        </div>"""

target_str = 'id="cards-quatro-mares"></div>\n          </div>\n        </div>'
new_tide_html = html.replace(target_str, target_str + "\n\n" + insertion_html)
print("Replaced tide grid:", len(new_tide_html) > len(html))

# Now update dadosMaresSemana in new_tide_html
old_dados = html[idx_d:idx_d_end+2]
new_dados = """const dadosMaresSemana = [
      {
        diaRotulo: "Hoje",
        lua: "Lua Cheia",
        tipo: "Maré de Sizígia (Maré Grande)",
        alturaAtual: "1.2m",
        statusTexto: "Vazando",
        dica: "A baixa-mar abre excelentes coroas nas margens de São Lourenço para cata de marisco e unhas-de-velho.",
        janelaMangueHorario: "07:00 às 11:30",
        janelaMangueDetalhe: "Vaza seca a lama a partir das 07h. <strong>Reponta da maré às 12h00</strong>: comece a recolher e saia do mangue fundo até 11h30 para não atolar ou ficar ilhado.",
        janelaMangueTempo: "Tempo útil: ~4h30",
        janelaComportasHorario: "15:15 às 17:10",
        janelaComportasDetalhe: "Maré atinge nível de renovação <strong>100% por gravidade</strong> (Pico de 2.4m às 15:58). Economia de bombas e combustível.",
        janelaComportasTempo: "Janela: ~2h00 de cota cheia",
        eventos: [
          { hora: "03:22", tipo: "Preamar (Cheia)", altura: "2.3m", icone: "fa-arrow-up", cor: "text-sky-400" },
          { hora: "09:40", tipo: "Baixa-mar (Seca)", altura: "0.2m", icone: "fa-arrow-down", cor: "text-amber-400" },
          { hora: "15:58", tipo: "Preamar (Cheia)", altura: "2.4m", icone: "fa-arrow-up", cor: "text-sky-400" },
          { hora: "22:15", tipo: "Baixa-mar (Seca)", altura: "0.3m", icone: "fa-arrow-down", cor: "text-amber-400" }
        ]
      },
      {
        diaRotulo: "Amanhã",
        lua: "Lua Cheia",
        tipo: "Maré de Sizígia (Pico Forte)",
        alturaAtual: "1.6m",
        statusTexto: "Enchendo",
        dica: "Preamar baterá 2.5m à tarde: volume ideal para renovar as comportas dos tanques de camarão.",
        janelaMangueHorario: "07:45 às 12:15",
        janelaMangueDetalhe: "Seca extrema (0.1m às 10:22): vaza muito profunda e coroas abertas. Sair até 12h15 antes da reponta forte.",
        janelaMangueTempo: "Tempo útil: ~4h30",
        janelaComportasHorario: "15:55 às 17:50",
        janelaComportasDetalhe: "Pico máximo de 2.5m às 16:40. Volume excelente para abastecimento e sangria geral dos viveiros.",
        janelaComportasTempo: "Janela: ~2h00 de cota cheia",
        eventos: [
          { hora: "04:05", tipo: "Preamar (Cheia)", altura: "2.4m", icone: "fa-arrow-up", cor: "text-sky-400" },
          { hora: "10:22", tipo: "Baixa-mar (Seca)", altura: "0.1m", icone: "fa-arrow-down", cor: "text-amber-400" },
          { hora: "16:40", tipo: "Preamar (Cheia)", altura: "2.5m", icone: "fa-arrow-up", cor: "text-sky-400" },
          { hora: "22:58", tipo: "Baixa-mar (Seca)", altura: "0.2m", icone: "fa-arrow-down", cor: "text-amber-400" }
        ]
      },
      {
        diaRotulo: "+2 Dias",
        lua: "Lua Cheia",
        tipo: "Maré Grande",
        alturaAtual: "0.9m",
        statusTexto: "Baixa-mar",
        dica: "Seca funda pela manhã no estuário para mariscagem.",
        janelaMangueHorario: "08:30 às 13:00",
        janelaMangueDetalhe: "Excelente para cata de marisco branco e unhas-de-velho nas coroas pela manhã. Sair até 13h00.",
        janelaMangueTempo: "Tempo útil: ~4h30",
        janelaComportasHorario: "16:40 às 18:30",
        janelaComportasDetalhe: "Renovação rápida aproveitando o pico de 2.4m no final da tarde.",
        janelaComportasTempo: "Janela: ~1h50 de cota cheia",
        eventos: [
          { hora: "04:48", tipo: "Preamar (Cheia)", altura: "2.3m", icone: "fa-arrow-up", cor: "text-sky-400" },
          { hora: "11:05", tipo: "Baixa-mar (Seca)", altura: "0.2m", icone: "fa-arrow-down", cor: "text-amber-400" },
          { hora: "17:25", tipo: "Preamar (Cheia)", altura: "2.4m", icone: "fa-arrow-up", cor: "text-sky-400" },
          { hora: "23:42", tipo: "Baixa-mar (Seca)", altura: "0.3m", icone: "fa-arrow-down", cor: "text-amber-400" }
        ]
      },
      {
        diaRotulo: "+3 Dias",
        lua: "Minguante Desse",
        tipo: "Início de Maré Quebrada",
        alturaAtual: "1.4m",
        statusTexto: "Águas Calmas",
        dica: "Correnteza mais branda no Rio Goiana, excelente para pesca de siri e tarrafa.",
        janelaMangueHorario: "09:15 às 13:45",
        janelaMangueDetalhe: "Maré quebrada com menor velocidade de correnteza. Janela favorável no mangue até 13h45.",
        janelaMangueTempo: "Tempo útil: ~4h30",
        janelaComportasHorario: "17:30 às 19:15",
        janelaComportasDetalhe: "Cota suficiente (2.2m) para reforço de oxigenação nas comportas principais.",
        janelaComportasTempo: "Janela: ~1h45 de cota cheia",
        eventos: [
          { hora: "05:32", tipo: "Preamar (Cheia)", altura: "2.1m", icone: "fa-arrow-up", cor: "text-sky-400" },
          { hora: "11:50", tipo: "Baixa-mar (Seca)", altura: "0.4m", icone: "fa-arrow-down", cor: "text-amber-400" },
          { hora: "18:12", tipo: "Preamar (Cheia)", altura: "2.2m", icone: "fa-arrow-up", cor: "text-sky-400" },
          { hora: "00:29", tipo: "Baixa-mar (Seca)", altura: "0.5m", icone: "fa-arrow-down", cor: "text-amber-400" }
        ]
      }
    ];"""

new_tide_html = new_tide_html.replace(old_dados, new_dados)
print("Updated dadosMaresSemana:", "janelaMangueHorario" in new_tide_html)

# Update renderizarMare function to update the DOM elements
old_render_start = "document.getElementById('resumo-mare-topo').innerText = `${d.statusTexto} (${d.alturaAtual})`;"
new_render_add = """document.getElementById('resumo-mare-topo').innerText = `${d.statusTexto} (${d.alturaAtual})`;

      // Atualiza Calculadora de Janela de Trabalho e Comportas
      const elJmH = document.getElementById('janela-mangue-horario');
      if (elJmH) elJmH.innerText = d.janelaMangueHorario;
      const elJmD = document.getElementById('janela-mangue-detalhe');
      if (elJmD) elJmD.innerHTML = d.janelaMangueDetalhe;
      const elJmS = document.getElementById('janela-mangue-seguro');
      if (elJmS) elJmS.innerText = d.janelaMangueTempo;

      const elJcH = document.getElementById('janela-comportas-horario');
      if (elJcH) elJcH.innerText = d.janelaComportasHorario;
      const elJcD = document.getElementById('janela-comportas-detalhe');
      if (elJcD) elJcD.innerHTML = d.janelaComportasDetalhe;
      const elJcT = document.getElementById('janela-comportas-tempo');
      if (elJcT) elJcT.innerText = d.janelaComportasTempo;"""

new_tide_html = new_tide_html.replace(old_render_start, new_render_add)
print("Updated renderizarMare:", "elJmH" in new_tide_html)

# Write to index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_tide_html)

print("index.html successfully updated!")