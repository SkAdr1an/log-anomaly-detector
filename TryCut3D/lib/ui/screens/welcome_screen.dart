import 'package:flutter/material.dart';
import 'package:trycut3d/ui/components/avatar_panel.dart';

class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          // FUNDO
          Container(
            decoration: const BoxDecoration(
              image: DecorationImage(
                image: AssetImage('assets/images/fundo_app.png'),
                fit: BoxFit.cover,
              ),
            ),
          ),

          // TELA INTERATIVA COM CONTEÚDO CENTRAL
          SafeArea(
            child: Column(
              children: [
                const SizedBox(height: 60),

                // TÍTULO ESTÁTICO ESTILIZADO
                const Center(
                  child: Text(
                    'ENCONTRE SEU CORTE',
                    style: TextStyle(
                      fontSize: 30,
                      fontFamily: 'Orbitron',
                      fontWeight: FontWeight.bold,
                      color: Colors.cyanAccent,
                      letterSpacing: 2,
                      shadows: [
                        Shadow(
                          color: Colors.cyanAccent,
                          blurRadius: 20,
                          offset: Offset(0, 0),
                        ),
                      ],
                    ),
                    textAlign: TextAlign.center,
                  ),
                ),

                const Spacer(),

                // AVATAR PRINCIPAL NO PAINEL 3D
                const AvatarPanel(),

                const Spacer(),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
