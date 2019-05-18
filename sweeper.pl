% Inicio busca em profundidade

solucao_bp(Inicial,Solucao) :-
  bp([],Inicial,Solucao).

bp(Caminho,Estado,[Estado|Caminho]) :-
  meta(Estado).

bp(Caminho,Estado,Solucao) :-
  s(Estado,Sucessor),
  not(pertence(Sucessor,[Estado|Caminho])),
  bp([Estado|Caminho],Sucessor,Solucao).

concatena([ ],L,L).
concatena([Cab|Cauda],L2,[Cab|Resultado]) :-
  concatena(Cauda,L2,Resultado).

pertence(Elem,[Elem|_ ]).
pertence(Elem,[ _| Cauda]) :-
  pertence(Elem,Cauda).

% Fim busca em profundidade

% Inicio do CAOS

% [ [Robo_X, Robo_Y, Qnt_Lixo_Robo], [Dock_X,Dock_Y], [Mapa_X,Mapa_Y,Quantidade_Total_Lixo], Lista_Lixos, Lista_Lixeiras, Lista_Elevadores]
%

% Função auxiliar para remover elemento de uma lista
del(X,[X|Tail],Tail).
del(X,[Y|Tail],[Y|Tail1]):-
    del(X,Tail,Tail1).

% Função auxiliar para substituir um elemento em uma lista
replace(I, L, E, K) :-
  nth0(I, L, _, R),
  nth0(I, K, E, R).

% Função para a locomoção no elevador
s(Estado,Sucessor):-
  nth0(0, Estado, [Robo_X,Robo_Y,Robo_Lixo]),
  nth0(5, Estado, Elevadores),
  pertence([Robo_X,Robo_Y],Elevadores),
  % Checagens não são necessárias.
  Robo_Y >= 0,
  (Y is Robo_Y+1;Y is Robo_Y-1),
  pertence([Robo_X,Y],Elevadores),
  replace(0, Estado, [Robo_X,Y,Robo_Lixo], Sucessor).

% Encontra lixeira e esvazia
s(Estado,Sucessor):-
  nth0(0, Estado, [Robo_X,Robo_Y,Robo_Lixo]),
  nth0(4, Estado, Lixeiras),
  pertence([Robo_X,Robo_Y],Lixeiras),
  QntNovaDeLixo is 0,
  Robo_Lixo >= 0,
  Robo_Lixo < 3,
  replace(0, Estado, [Robo_X,Robo_Y,QntNovaDeLixo], Sucessor).

% Pega lixo do mapa
s(Estado,Sucessor):-
  nth0(0, Estado, [Robo_X,Robo_Y,Robo_Lixo]),
  nth0(2, Estado, [Mapa_X,Mapa_Y,Total_Lixos]),
  nth0(3, Estado, Lixos),
  Robo_Lixo < 3,
  pertence([Robo_X,Robo_Y],Lixos),
  del([Robo_X,Robo_Y],Lixos,Nova_Lista_De_Lixos),
  Qnt_Lixo_No_Mapa is Total_Lixos-1,
  Qnt_Lixo_No_Robo is Robo_Lixo+1,
  % S0 é estado auxiliar
  replace(0, Estado, [Robo_X,Robo_Y,Qnt_Lixo_No_Robo], S0),
  % S0 é estado auxiliar
  replace(2, S0, [Mapa_X,Mapa_Y,Qnt_Lixo_No_Mapa], S),
  replace(3, S, Nova_Lista_De_Lixos, Sucessor).

% Anda para esquerda ou direita
s(Estado,Sucessor):-
  nth0(0, Estado, [Robo_X,Robo_Y,Robo_Lixo]),
  nth0(2, Estado, [Mapa_X,_,_]),
  Robo_X < Mapa_X,
  Robo_X >= 0,
  (X is Robo_X+1;X is Robo_X-1),
  replace(0, Estado, [X,Robo_Y,Robo_Lixo], Sucessor).

meta(Estado):-
  nth0(0, Estado, [Robo_X,Robo_Y, Qnt_Lixo]),
  nth0(1, Estado, [Dock_X,Dock_Y]),
  nth0(2, Estado, [_,_,Total]),
  Robo_X = Dock_X,
  Robo_Y = Dock_Y,
  Total = 0,
  Qnt_Lixo = 0.
