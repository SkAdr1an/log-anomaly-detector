import 'package:flutter/material.dart';
import 'package:model_viewer_plus/model_viewer_plus.dart';

class AvatarPanel extends StatelessWidget {
  const AvatarPanel({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        width: 260,
        height: 360,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(32),
          border: Border.all(
            color: Colors.cyanAccent.withOpacity(0.8),
            width: 2,
          ),
          boxShadow: [
            BoxShadow(
              color: Colors.cyanAccent.withOpacity(0.4),
              blurRadius: 30,
              spreadRadius: 5,
            ),
          ],
        ),
        child: ClipRRect(
          borderRadius: BorderRadius.circular(32),
          child: ModelViewer(
            src: 'assets/models/avatar_negro.glb',
            alt: 'Avatar 3D',
            autoRotate: true,
            cameraControls: true,
            disableZoom: true,
            ar: false,
            backgroundColor: Colors.transparent,
          ),
        ),
      ),
    );
  }
}
