//*********************************************************
//
// Copyright (c) Microsoft. All rights reserved.
// This code is licensed under the MIT License (MIT).
// THIS CODE IS PROVIDED *AS IS* WITHOUT WARRANTY OF
// ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY
// IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR
// PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.
//
//*********************************************************

#pragma once

#include "Common\DeviceResources.h"

namespace HolographicFaceTracker
{
    class TextRenderer : public DX::Resource
    {
    public:
        TextRenderer(
            std::shared_ptr<DX::DeviceResources> deviceResources,
            uint32_t textureWidth,
            uint32_t textureHeight);

        void RenderTextOffscreen(std::wstring const& str, bool isAuthorized, Windows::Foundation::Numerics::float2 position);

        concurrency::task<void> CreateDeviceDependentResourcesAsync() override;
        void ReleaseDeviceDependentResources() override;

        ID3D11ShaderResourceView* GetTexture() const { return m_shaderResourceView.Get();   };
        ID3D11SamplerState*       GetSampler() const { return m_pointSampler.Get();         };
		std::wstring                             pre_sentence_pre;

		void SetTargetPosition(Windows::Foundation::Numerics::float3 pos) { m_position = pos; }

    private:
        // Direct3D resources for rendering text to an off-screen render target.
        Microsoft::WRL::ComPtr<ID3D11Texture2D>             m_texture;
        Microsoft::WRL::ComPtr<ID3D11ShaderResourceView>    m_shaderResourceView;
        Microsoft::WRL::ComPtr<ID3D11SamplerState>          m_pointSampler;
        Microsoft::WRL::ComPtr<ID3D11RenderTargetView>      m_renderTargetView;
        Microsoft::WRL::ComPtr<ID2D1RenderTarget>           m_d2dRenderTarget;
        Microsoft::WRL::ComPtr<ID2D1SolidColorBrush>        m_whiteBrush;
        Microsoft::WRL::ComPtr<IDWriteTextFormat>           m_textFormat;

		// For setting position
		Windows::Foundation::Numerics::float3           m_position = { 0.f, 0.f, -2.f };

        // CPU-based variables for configuring the offscreen render target.
        const unsigned int m_textureWidth;
        const unsigned int m_textureHeight;
    };
}
