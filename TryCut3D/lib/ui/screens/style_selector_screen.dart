import 'package:flutter/material.dart';

class StyleSelectorScreen extends StatelessWidget {
  const StyleSelectorScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Selecionar Estilo')),
      body: const Center(child: Text('Tela de seleção de estilo')),
    );
  }
}
