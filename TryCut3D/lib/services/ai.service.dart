class AIService {
  // Simula a sugestão com base no tipo de cabelo e etnia
  List<HaircutModel> suggestHaircuts(UserModel user) {
    // Exemplo estático, substituível por API futuramente
    return [
      HaircutModel(
        name: 'Corte Baixo com Desenho',
        imagePath: 'assets/images/corte1.png',
        recommendedFor: 'Afro/Crespo',
      ),
      HaircutModel(
        name: 'Degradê com topo alto',
        imagePath: 'assets/images/corte2.png',
        recommendedFor: 'Afro/Crespo',
      ),
      HaircutModel(
        name: 'Corte Tradicional',
        imagePath: 'assets/images/corte3.png',
        recommendedFor: 'Todos',
      ),
    ];
  }
}
